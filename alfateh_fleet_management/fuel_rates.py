# -*- coding: utf-8 -*-

from openerp import models, fields, api
# Route Management
class fuel_rate(models.Model):
	_name = 'fuel.rate'
	fuel_gasoline_rate = fields.Float('Gasoline')
	fuel_hioctane_rate = fields.Float('Hioctane')
	fuel_cng_rate = fields.Float('CNG')
	fuel_disel_rate = fields.Float('DISEL')


class fuel_type(models.Model):
	_inherit = 'fleet.vehicle'
	fuel_type = fields.Selection([('gasoline', 'Gasoline'), ('diesel', 'Diesel'), ('hioctane', 'Hioctane'), ('cng', 'CNG')], 'Fuel Type', help='Fuel Used by the vehicle')