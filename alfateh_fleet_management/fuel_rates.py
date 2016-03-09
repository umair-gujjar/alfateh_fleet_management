# -*- coding: utf-8 -*-

from openerp import models, fields, api
# Route Management
class fuel_rate(models.Model):
	_name = 'fuel.rate'
	fuel_gasoline_rate = fields.Float('Gasoline',select=True)
	fuel_hioctane_rate = fields.Float('Hi-Octane')
	fuel_cng_rate = fields.Float('CNG')
	fuel_disel_rate = fields.Float('Diesel')


class fuel_type(models.Model):
	_inherit = 'fleet.vehicle'
	fuel_type = fields.Selection([('fuel_gasoline_rate', 'Gasoline'), ('fuel_disel_rate', 'Diesel'), ('fuel_hioctane_rate', 'Hi-Octane'), ('fuel_cng_rate', 'CNG')], 'Fuel Type',select=True, help='Fuel Used by the vehicle')