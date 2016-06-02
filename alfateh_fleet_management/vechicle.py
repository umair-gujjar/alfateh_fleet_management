from openerp import models, fields, api
import datetime
from datetime import date, datetime
import time

class alfateh_fleet_management(models.Model):
	_inherit = 'fleet.vehicle'
	engine_num = fields.Char('Engine Number')
	average_consumption = fields.Float('Average Consumption')
	expiry_token = fields.Date('Expiry Token')
	capacity = fields.Char('Capacity')
	vehicle_status = fields.Char('Vehicle Status')
	engine_oil_change = fields.Integer('Engine Oil Change')
	oil_filter = fields.Integer('Oil Filter')
	air_filter = fields.Integer('Air Filter')
	brake_oil = fields.Char('Brake Oil')
	gear_oil = fields.Integer('Gear Oil')
	wheel_alignment = fields.Char('Wheel Alignment')
	kamani = fields.Char('Kamani')
	batteries = fields.Char('Batteries')
	power_steering_oil = fields.Char('Power Steering Oil')
	greecing = fields.Char('Greecing')
	engine_oil_change_value = fields.Float(string='Odometer (Engine Oil)')
	oil_filter_value = fields.Float('Odometer (Oil Filter)')
	air_filter_value = fields.Float('Odometer (Air Filter)')
	gear_oil_value = fields.Float('Odometer (Gear Oil)')
	engine_oil_chk_box = fields.Boolean(string='Engine Oil', compute='_compute_odometer_value')
	oil_filter_chk_box = fields.Boolean(string='Oil Filter', compute='_compute_odometer_value')
	air_filter_chk_box = fields.Boolean(string='Air Filter', compute='_compute_odometer_value')
	gear_oil_chk_box = fields.Boolean(string='Gear Oil', compute='_compute_odometer_value')
	@api.one
	@api.depends('odometer')
	def _compute_odometer_value(self):
		if self.odometer > self.gear_oil_value:
			self.gear_oil_chk_box = True
		if self.odometer > self.air_filter_value:
			self.air_filter_chk_box = True
		if self.odometer > self.oil_filter_value:
			self.oil_filter_chk_box = True
		if self.odometer > self.engine_oil_change_value:
			self.engine_oil_chk_box = True

class alfateh_vehicle_cost(models.Model):
	_inherit = 'fleet.vehicle.cost'
	vehicle_trip = fields.Many2one('trip.management', string="Trip" ,domain="[('date','=',date)]")


class fuel_log(models.Model):
	_inherit = 'fleet.vehicle.log.fuel'
	card_name = fields.Many2one('fuelcard.management',string='Card Name', required=True)
	odoo_meter = fields.Float(string='Odometer Value')
	fuel_type = fields.Selection([('fuel_gasoline_rate', 'Gasoline'), ('fuel_disel_rate', 'Diesel'), ('fuel_hioctane_rate', 'Hi-Octane'), ('fuel_cng_rate', 'CNG')], 'Fuel Type', help='Fuel Used by the vehicle')

	@api.onchange('card_name')
	def testing_lter_change(self):
		if self.vehicle_id:
			self.fuel_type	= self.vehicle_id.fuel_type
	@api.onchange('fuel_type')
	def onchange_atfc_atoc_field(self):
		fuel_rate_rec = self.env['fuel.rate']
		if self.fuel_type:
			if self.fuel_type == 'fuel_gasoline_rate':
				self.price_per_liter = fuel_rate_rec.search([]).fuel_gasoline_rate 
			elif self.fuel_type == 'fuel_hioctane_rate':
				self.price_per_liter = fuel_rate_rec.search([]).fuel_hioctane_rate 
			elif self.fuel_type == 'fuel_cng_rate':
				self.price_per_liter = fuel_rate_rec.search([]).fuel_cng_rate 
			else:
				self.price_per_liter = fuel_rate_rec.search([]).fuel_disel_rate 
class fuel_service_log(models.Model):
	_inherit = 'fleet.vehicle.log.services'
	engine_oil_change_value = fields.Float('Odometer (Engine Oil)')
	oil_filter_value = fields.Float('Odometer (Oil Filter)')
	air_filter_value = fields.Float('Odometer (Air Filter)')
	gear_oil_value = fields.Float('Odometer (Gear Oil)')
	@api.model
	def create(self, vals):
		current_vehicles = self.env['fleet.vehicle'].search([('id','=',vals['vehicle_id'])])
		current_vehicles.engine_oil_change_value = current_vehicles.engine_oil_change_value + vals['engine_oil_change_value']
		current_vehicles.oil_filter_value = current_vehicles.oil_filter_value + vals['oil_filter_value']
		current_vehicles.air_filter_value = current_vehicles.air_filter_value + vals['air_filter_value']
		current_vehicles.gear_oil_value = current_vehicles.gear_oil_value + vals['gear_oil_value']
		return super(fuel_service_log,self).create(vals)
	@api.multi
	def write(self, vals):
		before_engine_oil_change_value = self.engine_oil_change_value
		before_oil_filter_value = self.oil_filter_value
		before_air_filter_value = self.air_filter_value
		before_gear_oil_value = self.gear_oil_value
		result =  super(fuel_service_log,self).write(vals)
		self.vehicle_id.engine_oil_change_value = (self.vehicle_id.engine_oil_change_value + self.engine_oil_change_value) - before_engine_oil_change_value
		self.vehicle_id.oil_filter_value = (self.vehicle_id.oil_filter_value + self.oil_filter_value) - before_oil_filter_value
		self.vehicle_id.air_filter_value = (self.vehicle_id.air_filter_value + self.air_filter_value) - before_air_filter_value
		self.vehicle_id.gear_oil_value = (self.vehicle_id.gear_oil_value + self.gear_oil_value) - before_gear_oil_value
		return result

	@api.multi
	def unlink(self):
		current_vehicles = self.env['fleet.vehicle'].search([('id','=',self.vehicle_id.id)])
		current_vehicles.engine_oil_change_value = current_vehicles.engine_oil_change_value - self.engine_oil_change_value
		current_vehicles.oil_filter_value = current_vehicles.oil_filter_value - self.oil_filter_value
		current_vehicles.air_filter_value = current_vehicles.air_filter_value - self.air_filter_value
		current_vehicles.gear_oil_value = current_vehicles.gear_oil_value - self.gear_oil_value
		return super(fuel_service_log,self).unlink()