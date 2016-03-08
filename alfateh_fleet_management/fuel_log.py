# -*- coding: utf-8 -*-

from openerp import models, fields, api
# Route Management
class fuel_log(models.Model):
	_inherit = 'fleet.vehicle.log.fuel'


	@api.onchange('liter')
	def testing_lter_change(self):
		print self.liter
	


