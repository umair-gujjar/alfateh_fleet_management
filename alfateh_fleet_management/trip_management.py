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
	route_distance = fields.Float('Route Distance')
	projected_trip_time = fields.Float('Projected Time')
	projected_trip_fuel = fields.Float('Projected Fuel')
	projected_trip_fuel_cost = fields.Float('Projected Fuel Cost')
	projected_trip_other_cost = fields.Float('Projected Other Cost')
	projected_trip_cost = fields.Float('Projected Total Cost')	
	actual_trip_time = fields.Float('Actual Time')
	actual_trip_fuel = fields.Float('Actual Fuel')
	actual_trip_fuel_cost = fields.Float('Actual Fuel Cost')
	actual_trip_other_cost = fields.Float('Actual Other Cost ')
	actual_trip_cost = fields.Float('Actual Total Cost ')
	variance_trip_time = fields.Float('variance Time')
	variance_trip_fuel = fields.Float('variance Fuel')
	variance_trip_fuel_cost = fields.Float('variance Fuel Cost')
	variance_trip_other_cost = fields.Float('variance Other Cost ')
	variance_trip_cost = fields.Float('variance Total Cost ')
	trip_description = fields.Text('Description')
	_defaults = {
    'date': datetime.now(),
    }
	#def create(self, cr, uid, vals, context=None):
	#	sequence=self.pool.get('ir.sequence').get(cr, uid, 'trip.management')
	#	vals['seq']=sequence
	#	return super(trip_management, self).create(cr, uid, vals, context=context)
	
	
	@api.onchange('route','vehicle')
	def onchange_route_field(self):
		#check_vehcile = self.env['trip.management'].search([])
		if self.vehicle:
			self.route_distance = self.route.route_distance
			self.projected_trip_time = self.route.route_time
			if self.vehicle.average_consumption:
				self.projected_trip_fuel = self.route_distance / self.vehicle.average_consumption 
			self.projected_trip_cost = self.route.route_total_cost

			if self.route.name:
				self.name = self.date+" "+ self.route.name


	@api.onchange('actual_trip_fuel_cost','actual_trip_other_cost')
	def onchange_atfc_atoc_field(self):
		if self.actual_trip_fuel_cost or self.actual_trip_other_cost:
			self.actual_trip_cost = self.actual_trip_fuel_cost + self.actual_trip_other_cost

	@api.onchange('projected_trip_time','actual_trip_time','projected_trip_fuel','actual_trip_fuel','projected_trip_fuel_cost','actual_trip_fuel_cost'
		,'projected_trip_other_cost','actual_trip_other_cost','projected_trip_cost','actual_trip_cost')
	def onchange_variance_field(self):
		if self.projected_trip_time or self.actual_trip_time or self.projected_trip_fuel or self.actual_trip_fuel or self.projected_trip_fuel_cost or self.actual_trip_fuel_cost or self.projected_trip_other_cost or self.actual_trip_other_cost or self.projected_trip_cost or self.actual_trip_cost:

			self.variance_trip_time =  self.actual_trip_time - self.projected_trip_time

			self.variance_trip_fuel =  self.actual_trip_fuel - self.projected_trip_fuel

			self.variance_trip_fuel_cost =  self.actual_trip_fuel_cost - self.projected_trip_fuel_cost

			self.variance_trip_other_cost =  self.actual_trip_other_cost - self.projected_trip_other_cost

			self.variance_trip_cost =  self.actual_trip_cost - self.projected_trip_cost

	#def act_show_log_cost(self, cr, uid, ids, context=None):
	#	if context is None:
	#		context = {}
	#	res = self.pool.get('ir.actions.act_window').for_xml_id(cr, uid ,'fleet','fleet_vehicle_costs_act', context=context)
	#	res['context'] = context
	#	res['context'].update({
	#		'default_vehicle_id': ids[0],
	#		'search_default_parent_false': True
	#		})
	#	res['domain'] = [('vehicle_id','=', ids[0])]
	#	return res	

	def act_show_log_cost(self):
		self.ensure_one()
		self.name = "New name"
		return {
			'context': self.env.context,
			'view_type': 'form',
			'view_mode': 'form',
			'res_model': 'fleet_vehicle_costs_act',
			'res_id': self.id,
			'view_id': False,
			'type': 'ir.actions.act_window',
			'target': 'new',
		}

