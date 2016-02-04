# -*- coding: utf-8 -*-

from openerp import models, fields, api

# Trip Mangement
class trip_management(models.Model):
	_name = 'trip.management'
	_inherit = ['mail.thread', 'ir.needaction_mixin']
	name = fields.Char('Name')
	vehicle = fields.Many2one('fleet.vehicle','Vehicle')
	route = fields.Many2one('route.management','Route')
	route_distance = fields.Float('Route Distance')
	projected_trip_time = fields.Float('Projected Time')
	projected_trip_fuel = fields.Float('Projected Fuel')
	projected_trip_cost = fields.Float('Projected Cost')	
	actual_trip_time = fields.Float('Actual Time')
	actual_trip_fuel = fields.Float('Actual Fuel')
	actual_trip_cost = fields.Float('Actual Cost')
	trip_cost = fields.Float('Trip Total Cost')
	@api.onchange('route')
	def onchange_route_field(self):
		self.route_distance = self.route.route_distance
		self.projected_trip_time = self.route.route_time
		self.projected_trip_fuel = self.route.route_fuel
		self.projected_trip_cost = self.route.route_cost