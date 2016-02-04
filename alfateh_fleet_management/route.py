# -*- coding: utf-8 -*-

from openerp import models, fields, api

# Route Management
class route_management(models.Model):
	_name = 'route.management'
	_inherit = ['mail.thread', 'ir.needaction_mixin']
	route_defination = fields.Char('Route Defination')
	route_time = fields.Float('Time(hours)')
	route_distance = fields.Float('Distance(km)')
	route_fuel = fields.Float('Fuel(liters)')
	route_cost = fields.Float('Cost')

