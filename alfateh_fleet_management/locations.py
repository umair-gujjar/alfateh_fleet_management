# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import ValidationError


# Route Management
class route_location(models.Model):
	_name = 'route.locations'
	name = fields.Char('Location')
	#mobile = fields.Char('Location')
	_sql_constraints = [
    ('name_unique', 'unique(name)', 'This Location already exists!')
	]
	
				
				
	