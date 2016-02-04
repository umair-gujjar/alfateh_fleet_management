# -*- coding: utf-8 -*-

from openerp import models, fields, api

# Trip Mangement
class trip_management(models.Model):
	_name = 'trip.management'
	_inherit = ['mail.thread', 'ir.needaction_mixin']
	name = fields.Float('Name')
	route_distance = fields.Float('KM')
	trip_cost = fields.Float('Trip Total Cost')
	projected_trip_cost = fields.Float('Projected Cost')
	actual_trip_cost = fields.Float('Actual Cost')
	vehicle = fields.Many2one('fleet.vehicle','Vehicle')


