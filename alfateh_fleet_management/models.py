# -*- coding: utf-8 -*-

from openerp import models, fields, api

class alfateh_fleet_management(models.Model):
	_inherit = 'fleet.vehicle'
	engine_num = fields.Char('Engine Num')
	average_consumption = fields.Float('Average Consumption')
	expiry_token = fields.Date('Expiry Token')

# Trip Mangement
class trip_management(models.Model):
	_name = 'trip.management'
	_inherit = ['mail.thread', 'ir.needaction_mixin']
	route_distance = fields.Float('KM')
	trip_cost = fields.Float('Trip Total Cost')
	projected_trip_cost = fields.Float('Projected Cost')
	actual_trip_cost = fields.Float('Actual Cost')
	vehicle = fields.Many2one('fleet.vehicle','Vehicle')

# Route Management
class route_management(models.Model):
	_name = 'route.management'
	route_def = fields.Char('Route Defination')
	route_time = fields.Float('Time')
	route_distance = fields.Float('KM')


