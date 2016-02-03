# -*- coding: utf-8 -*-

from openerp import models, fields, api

class alfateh_fleet_management(models.Model):
	_inherit = 'fleet.vehicle'
	engine_num = fields.Char('Engine Num')
	average_consumption = fields.Float('Average Consumption')
	expiry_token = fields.Date('Expiry Token')
