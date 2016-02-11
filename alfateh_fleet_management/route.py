# -*- coding: utf-8 -*-

from openerp import models, fields, api
# Route Management
class route_management(models.Model):
	_name = 'route.management'
	_inherit = ['mail.thread', 'ir.needaction_mixin']
	name = fields.Char('Name' ,readonly= True)
	route_defination = fields.Many2many('route.locations',string='Route Defination')
	route_time = fields.Float('Time(hours)')
	route_distance = fields.Float('Distance(km)')
	route_fuel = fields.Float('Fuel(liters)')
	route_fuel_cost = fields.Float('Fuel Cost')
	route_other_cost = fields.Float('Other Cost')
	route_total_cost = fields.Float('Total Cost')
	route_description = fields.Text('Description')


	_sql_constraints = [
    ('name_unique', 'unique(name)', 'This Route already exists!')
	]


	@api.onchange('route_defination')
	def route_defination_name_get(self):
		let_say_name = self.name
		recs_save_list = []   
		for i in self.route_defination:
			recs_save_list.append(i.name)
		#print recs_save_list
		self.name = ' --> '.join(recs_save_list)