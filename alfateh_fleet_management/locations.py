# -*- coding: utf-8 -*-

from openerp import models, fields, api

# Route Management
class route_location(models.Model):
	_name = 'route.locations'
	name = fields.Char('Location')
	

	