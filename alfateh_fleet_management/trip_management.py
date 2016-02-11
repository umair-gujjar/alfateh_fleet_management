# -*- coding: utf-8 -*-

from openerp import models, fields, api
import datetime
from datetime import date, datetime
import time
# Trip Mangement
class trip_management(models.Model):
	_name = 'trip.management'
	_inherit = ['mail.thread', 'ir.needaction_mixin']
	name = fields.Char('Name')
	#seq = fields.Char('Seq')
	date = fields.Date('Date', required=True)
	vehicle = fields.Many2one('fleet.vehicle','Vehicle')
	route = fields.Many2one('route.management','Route')
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
	trip_description = fields.Text('Description')
	_defaults = {
    'date': datetime.now(),
    }
	#def create(self, cr, uid, vals, context=None):
	#	sequence=self.pool.get('ir.sequence').get(cr, uid, 'trip.management')
	#	vals['seq']=sequence
	#	return super(trip_management, self).create(cr, uid, vals, context=context)

	@api.onchange('route')
	def onchange_route_field(self):
		self.route_distance = self.route.route_distance
		self.projected_trip_time = self.route.route_time
		self.projected_trip_fuel = self.route.route_fuel
		self.projected_trip_cost = self.route.route_cost
		if self.route.name:
			self.name = self.date+" "+ self.route.name


