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
	kamni = fields.Char('Kamni')
	batteries = fields.Char('Batteries')
	power_steering_oil = fields.Char('Power Steering Oil')
	greecing = fields.Char('Greecing')
	#vehicle_type_fleet = fields.Selection([
            #('Bus', 'Bus'),
            #('Truck', 'Truck'),
            #('Car', 'Car'),
            #('Auto_Rickshaw', 'Auto Rickshaw'),
            #('Van', 'Van'),
            #],default='', string="Select Vehicle Type",)


class alfateh_vehicle_cost(models.Model):
	_inherit = 'fleet.vehicle.cost'
	vehicle_trip = fields.Many2one('trip.management', string="Trip" ,domain="[('date','=',date)]")


class fuel_log(models.Model):
	_inherit = 'fleet.vehicle.log.fuel'
	card_name = fields.Many2one('fuelcard.management',string='Card Name')

	@api.onchange('card_name')
	def testing_lter_change(self):
		print self.card_name
	
	


