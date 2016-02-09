# -*- coding: utf-8 -*-

import datetime
from datetime import date, datetime
import time
from openerp import models, fields, api


# Fuel card Management
class fuelcards_management(models.Model):
	_name = 'fuelcard.management'
	_inherit = ['mail.thread', 'ir.needaction_mixin']
	card_name = fields.Char('Card Number')
	card_company = fields.Char('Company')
	card_limit = fields.Float('Limit( in liters)')
	card_issue_data = fields.Date('Issue Date')
	card_expiry_data = fields.Date('Expiry Date')
	card_description = fields.Text('Description')
	card_consume_amount = fields.Float('Consume Amount(Rs)')
	card_consume_liter = fields.Float('Consume liters')
	card_recharge_amount = fields.Float('Recharge Amount(Rs)')
	card_recharge_liter = fields.Float('Recharge liters')
	consume_id = fields.One2many('consume','fuelcard_consume_id',string='Details')


	_defaults = {
    'card_issue_data': datetime.now(),
	'card_expiry_data': datetime.now(),
    }
	

class consume(models.Model):
	_name = 'consume'
	card_consume_amount = fields.Float('Consume Amount(Rs)')
	card_consume_liter = fields.Float('Consume liters')
	fuelcard_consume_id = fields.Many2one('fuelcard.management',string='Consume')


	