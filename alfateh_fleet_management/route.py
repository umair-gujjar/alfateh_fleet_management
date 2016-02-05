# -*- coding: utf-8 -*-

from openerp import models, fields, api

# Route Management
class route_management(models.Model):
	_name = 'route.management'
	_inherit = ['mail.thread', 'ir.needaction_mixin']
	name = fields.Char('Name',readonly=True)
	route_defination = fields.Char('Route Defination')
	route_time = fields.Float('Time(hours)')
	route_distance = fields.Float('Distance(km)')
	route_fuel = fields.Float('Fuel(liters)')
	route_cost = fields.Float('Cost')
	route_description = fields.Text('Description')

	def create(self, cr, uid, vals, context=None):
		sequence=self.pool.get('ir.sequence').get(cr, uid, 'route.management')
		vals['name']=sequence
		return super(route_management, self).create(cr, uid, vals, context=context)