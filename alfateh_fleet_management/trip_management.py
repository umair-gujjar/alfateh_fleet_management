# -*- coding: utf-8 -*-

from openerp import models, fields, api
import datetime
from datetime import date, datetime
import time
from openerp.exceptions import ValidationError
# Trip Mangement
class trip_management(models.Model):
	_name = 'trip.management'
	_inherit = ['mail.thread', 'ir.needaction_mixin']
	name = fields.Char('Name')
	#seq = fields.Char('Seq')
	date = fields.Date('Date', required=True)
	vehicle = fields.Many2one('fleet.vehicle','Vehicle',required=True)
	route = fields.Many2one('route.management','Route',required=True)
	route_distance = fields.Float('Projected Route Distance')
	projected_trip_time = fields.Float('Projected Time')
	projected_trip_fuel = fields.Float('Projected Fuel')
	projected_trip_fuel_cost = fields.Float('Projected Fuel Cost')
	projected_trip_other_cost = fields.Float('Projected Other Cost')
	projected_trip_cost = fields.Float('Projected Total Cost')	
	actual_trip_time = fields.Float('Actual Time')
	actual_trip_fuel = fields.Float('Actual Fuel')
	actual_trip_fuel_cost = fields.Float('Actual Fuel Cost')
	actual_trip_route_distance = fields.Float('Actual Route Distance')
	actual_trip_other_cost = fields.Float('Actual Other Cost ')
	actual_trip_cost = fields.Float('Actual Total Cost ')
	variance_trip_time = fields.Float('Variance Time')
	variance_trip_fuel = fields.Float('Variance Fuel')
	variance_trip_fuel_cost = fields.Float('Variance Fuel Cost')
	variance_trip_other_cost = fields.Float('Variance Other Cost ')
	variance_trip_cost = fields.Float('Variance Total Cost ')
	variance_route_distance = fields.Float('Variance Route Distance')
	trip_description = fields.Text('Description')
	cost_count = fields.Integer(string="Costs",compute='compute_user_todo_count')
	driver_id = fields.Many2one('res.partner','Driver')

	_defaults = {
    'date': datetime.now(),
    }
	#def create(self, cr, uid, vals, context=None):
	#	sequence=self.pool.get('ir.sequence').get(cr, uid, 'trip.management')
	#	vals['seq']=sequence
	#	return super(trip_management, self).create(cr, uid, vals, context=context)
	@api.one
	def compute_user_todo_count(self):
		Cost = self.env['fleet.vehicle.cost']
		self.cost_count = Cost.search_count([('vehicle_id', '=', self.vehicle.id), ('parent_id', '=', False)])
	def act_show_log_cost_trip(self, cr, uid, ids, context=None):
		if context is None:
			context = {}
		current_trip = self.pool.get('trip.management').browse(cr, uid, ids[0], context)
		res = self.pool.get('ir.actions.act_window').for_xml_id(cr, uid ,'fleet','fleet_vehicle_costs_act', context=context)
		res['context'] = context
		res['context'].update({
			'default_vehicle_id': current_trip.vehicle.id,
			'search_default_parent_false': True,
			'default_date': current_trip.date,
			'default_vehicle_trip': current_trip.id
		})
		res['domain'] = [('vehicle_id','=', current_trip.vehicle.id)]
		return res

#for getting fuel cost
	@api.onchange('projected_trip_fuel')
	def onchange_projected_trip_fuel_field(self):
		fuel_rate_rec = self.env['fuel.rate']
		if self.projected_trip_fuel:
			if self.vehicle.fuel_type == 'fuel_gasoline_rate':
				self.projected_trip_fuel_cost = fuel_rate_rec.search([]).fuel_gasoline_rate * self.projected_trip_fuel
			elif self.vehicle.fuel_type == 'fuel_hioctane_rate':
				self.projected_trip_fuel_cost = fuel_rate_rec.search([]).fuel_hioctane_rate * self.projected_trip_fuel
			elif self.vehicle.fuel_type == 'fuel_cng_rate':
				self.projected_trip_fuel_cost = fuel_rate_rec.search([]).fuel_cng_rate * self.projected_trip_fuel
			else:
				self.projected_trip_fuel_cost = fuel_rate_rec.search([]).fuel_disel_rate * self.projected_trip_fuel

#for getting driver of selected vehicle
	#@api.onchange('vehicle')
	#def onchange_get_driver(self):
	#	if self.vehicle:
	#		self.driver_id = self.vehicle.driver_id

	@api.onchange('route','vehicle')
	def onchange_route_field(self):
		#check_vehcile = self.env['trip.management'].search([])
		if self.vehicle:
			self.route_distance = self.route.route_distance
			self.projected_trip_time = self.route.route_time
			if self.vehicle.average_consumption:
				self.projected_trip_fuel = self.route_distance / self.vehicle.average_consumption
				self.actual_trip_fuel = self.actual_trip_route_distance / self.vehicle.average_consumption 
			self.projected_trip_cost = self.route.route_total_cost
			self.projected_trip_other_cost = self.route.route_other_cost
			if self.route.name:
				self.name = self.date+" "+ self.route.name

#calculate actual total trip cost on changing values of actual fuel and actual other cost
	@api.onchange('actual_trip_fuel_cost','actual_trip_other_cost')
	def onchange_atfc_atoc_field(self):
		if self.actual_trip_fuel_cost or self.actual_trip_other_cost:
			self.actual_trip_cost = self.actual_trip_fuel_cost + self.actual_trip_other_cost

	@api.onchange('actual_trip_route_distance')
	def onchange_atrd_field(self):
			if self.vehicle.average_consumption:
				self.actual_trip_fuel = self.actual_trip_route_distance / self.vehicle.average_consumption 
#calculate projected total trip cost on changing values of projected fuel and projected other cost
	@api.onchange('projected_trip_fuel_cost','projected_trip_other_cost')
	def onchange_atfc_atoc_field1(self):
		if self.projected_trip_fuel_cost or self.projected_trip_other_cost:
			self.projected_trip_cost = self.projected_trip_fuel_cost + self.projected_trip_other_cost

	@api.onchange('projected_trip_time','actual_trip_time','projected_trip_fuel','actual_trip_fuel','projected_trip_fuel_cost','actual_trip_fuel_cost'
		,'projected_trip_other_cost','actual_trip_other_cost','projected_trip_cost','actual_trip_cost')
	def onchange_variance_field(self):
		if self.projected_trip_time or self.actual_trip_time or self.projected_trip_fuel or self.actual_trip_fuel or self.projected_trip_fuel_cost or self.actual_trip_fuel_cost or self.projected_trip_other_cost or self.actual_trip_other_cost or self.projected_trip_cost or self.actual_trip_cost:

			self.variance_trip_time =  self.actual_trip_time - self.projected_trip_time

			self.variance_trip_fuel =  self.actual_trip_fuel - self.projected_trip_fuel

			self.variance_trip_fuel_cost =  self.actual_trip_fuel_cost - self.projected_trip_fuel_cost

			self.variance_trip_other_cost =  self.actual_trip_other_cost - self.projected_trip_other_cost

			self.variance_trip_cost =  self.actual_trip_cost - self.projected_trip_cost
			self.variance_route_distance =  self.actual_trip_route_distance - self.route_distance

#update button for varience 
	@api.multi
	def variance_field_update_button(self):
		if self.projected_trip_time or self.actual_trip_time or self.projected_trip_fuel or self.actual_trip_fuel or self.projected_trip_fuel_cost or self.actual_trip_fuel_cost or self.projected_trip_other_cost or self.actual_trip_other_cost or self.projected_trip_cost or self.actual_trip_cost:

			self.variance_trip_time =  self.actual_trip_time - self.projected_trip_time

			self.variance_trip_fuel =  self.actual_trip_fuel - self.projected_trip_fuel

			self.variance_trip_fuel_cost =  self.actual_trip_fuel_cost - self.projected_trip_fuel_cost

			self.variance_trip_other_cost =  self.actual_trip_other_cost - self.projected_trip_other_cost

			self.variance_trip_cost =  self.actual_trip_cost - self.projected_trip_cost
			self.variance_route_distance =  self.actual_trip_route_distance - self.route_distance

#for getting actual fuel cost
	@api.onchange('actual_trip_fuel')
	def onchange_actual_trip_fuel_field(self):
		fuel_rate_rec = self.env['fuel.rate']
		if self.actual_trip_fuel:
			if self.vehicle.fuel_type == 'fuel_gasoline_rate':
				self.actual_trip_fuel_cost = fuel_rate_rec.search([]).fuel_gasoline_rate * self.actual_trip_fuel
			elif self.vehicle.fuel_type == 'fuel_hioctane_rate':
				self.actual_trip_fuel_cost = fuel_rate_rec.search([]).fuel_hioctane_rate * self.actual_trip_fuel
			elif self.vehicle.fuel_type == 'fuel_cng_rate':
				self.actual_trip_fuel_cost = fuel_rate_rec.search([]).fuel_cng_rate * self.actual_trip_fuel
			else:
				self.actual_trip_fuel_cost = fuel_rate_rec.search([]).fuel_disel_rate * self.actual_trip_fuel

class fleet_vehicle_cost_alfateh_custom(models.Model):
	_inherit = 'fleet.vehicle.cost'
	
	@api.model
	def create(self, values):
		result = super(fleet_vehicle_cost_alfateh_custom, self).create(values)
		if ('vehicle_trip' in values) and (values['vehicle_trip'] > 0):
			record_of_trip = self.env['trip.management'].search([('id','=',values['vehicle_trip'])])
			print record_of_trip.actual_trip_other_cost
			record_of_trip.actual_trip_other_cost = record_of_trip.actual_trip_other_cost + values['amount']
			record_of_trip.actual_trip_cost = record_of_trip.actual_trip_cost + values['amount']
		return result
	
	@api.multi
	def write(self, values):
		if self.vehicle_trip and (self.vehicle_trip > 0):
			record_of_trip = self.env['trip.management'].search([('id','=',self.vehicle_trip.id)])
			official_trip_amount = record_of_trip.actual_trip_other_cost
			last_amount = official_trip_amount - self.amount
			actual_trip_cost_amount = record_of_trip.actual_trip_cost - self.amount
			result =  super(fleet_vehicle_cost_alfateh_custom,self).write(values)
			record_of_trip.actual_trip_other_cost = last_amount + self.amount
			record_of_trip.actual_trip_cost = actual_trip_cost_amount + self.amount
			return result

	@api.multi
	def unlink(self):
		record_of_trip = self.env['trip.management'].search([('id','=',self.vehicle_trip.id)])
		record_of_trip.actual_trip_other_cost = record_of_trip.actual_trip_other_cost - self.amount
		record_of_trip.actual_trip_cost = record_of_trip.actual_trip_cost - self.amount
		return super(fleet_vehicle_cost_alfateh_custom,self).unlink()