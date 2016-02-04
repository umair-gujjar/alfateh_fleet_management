# -*- coding: utf-8 -*-

from openerp import models, fields, api

# Route Management
class fuelcards_management(models.Model):
	_name = 'fuelcard.management'
	_inherit = ['mail.thread', 'ir.needaction_mixin']
	card_name = fields.Char('Card Name')
	card_company = fields.Char('Company')
	card_limit = fields.Float('Limit( in liters)')
	card_issue_data = fields.Date('Issue Date')
	card_expiry_data = fields.Date('Expiry Date')

