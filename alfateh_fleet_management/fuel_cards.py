# -*- coding: utf-8 -*-

import datetime
from datetime import date, datetime
import time
from openerp import models, fields, api


# Fuel card Management
class fuelcards_management(models.Model):
	_name = 'fuelcard.management'
	_inherit = ['mail.thread', 'ir.needaction_mixin']
	name = fields.Char('Card Number')
	card_company = fields.Char('Company')
	card_limit = fields.Float('Limit( in liters)')
	card_limit_remaining = fields.Float('Remaining Liters')
	card_issue_data = fields.Date('Issue Date')
	card_expiry_data = fields.Date('Expiry Date')
	card_description = fields.Text('Description')
	card_consume_amount = fields.Float('Consume Amount(Rs)')
	card_consume_liter = fields.Float('Consume liters')
	card_recharge_amount = fields.Float('Recharge Amount(Rs)')
	card_recharge_liter = fields.Float('Recharge liters')
	consume_id = fields.One2many('consume','fuelcard_consume_id',string='Details')
	recharge_id = fields.One2many('recharge','fuelcard_recharge_id',string='Details')
	recharge_count = fields.Integer(string="Recharge",compute='compute_user_todo_count')

	_defaults = {
	'card_issue_data': datetime.now(),
	}
	@api.onchange('card_limit')
	def limit_remaing_change(self):
		if self.card_limit:
			self.card_limit_remaining = self.card_limit	
	@api.one
	def compute_user_todo_count(self):
		recharge = self.env['recharge']
		self.recharge_count = recharge.search_count([('name', '=', self.id)])
	def act_show_log_recharge_trip(self, cr, uid, ids, context=None):
		if context is None:
			context = {}
		current_recharge = self.pool.get('fuelcard.management').browse(cr, uid, ids[0], context)
		recharageable_ltrs = current_recharge.card_limit - current_recharge.card_limit_remaining
		res = self.pool.get('ir.actions.act_window').for_xml_id(cr, uid ,'alfateh_fleet_management','action_fuelcard_recharge', context=context)
		res['context'] = context
		res['context'].update({
			'default_name': current_recharge.id,
			'default_card_recharge_liter' : recharageable_ltrs,
		})
		res['domain'] = [('name','=', current_recharge.id)]
		return res

	@api.one
	def recharge(self):
		if self.card_limit and self.card_limit_remaining:
			recharageable_ltrs = self.card_limit - self.card_limit_remaining
			if self.card_limit_remaining < self.card_limit:
				self.card_limit_remaining = self.card_limit_remaining + recharageable_ltrs
			else:
				self.card_limit_remaining = self.card_limit_remaining
class consume(models.Model):
	_name = 'consume'
	_inherit = ['mail.thread', 'ir.needaction_mixin']
	name = fields.Many2one('fuelcard.management','Card Number')
	card_consume_date = fields.Date('Date')
	card_consume_liter = fields.Float('Consume liters')
	card_consume_description = fields.Text('Description')
	card_available_liter = fields.Float('Available liters')
	fuelcard_consume_id = fields.Many2one('fuelcard.management',string='Consume')

	_defaults = {
    'card_consume_date': datetime.now(),
	'card_expiry_data': datetime.now(),
    }
	@api.onchange('name')
	def consume_name_change(self):
		if self.name:
			self.card_available_liter = self.name.card_limit_remaining
	@api.multi
	def write(self, values):
		result = super(consume, self).write(values)
		if self.card_consume_liter:
			available_limit = self.card_available_liter
			consume_limit = self.card_consume_liter
			remaining_limit = available_limit - consume_limit
		if self.card_consume_liter:
			self.name.card_limit_remaining = remaining_limit
		return result
	@api.one
	def push_values(self):
		available_limit = self.card_available_liter
		consume_limit = self.card_consume_liter
		remaining_limit = available_limit - consume_limit
		self.name.card_limit_remaining = remaining_limit



class recharge(models.Model):
	_name = 'recharge'
	_inherit = ['mail.thread', 'ir.needaction_mixin']
	name = fields.Many2one('fuelcard.management','Card Number')
	card_recharge_date = fields.Date('Date')
	card_recharge_liter = fields.Float('Recharge liters')
	card_recharge_description = fields.Text('Description')
	fuelcard_recharge_id = fields.Many2one('fuelcard.management',string='Recharge')

	_defaults = {
	'card_recharge_date': datetime.now(),
	}


class consumtion_fuel_log_model(models.Model):
	_inherit = 'fleet.vehicle.log.fuel'
#For create method code
	@api.model
	def create(self, vals):
		result = super(consumtion_fuel_log_model, self).create(vals)
		consumed_liter_fuel = vals['liter']
		#print vals['liter']
		#print vals.get('card_name')
		fuel_management_card = self.env['fuelcard.management'].search([('id','=', vals.get('card_name'))])
		remaining_fuel = fuel_management_card.card_limit_remaining - consumed_liter_fuel
		fuel_management_card.card_limit_remaining = remaining_fuel
		return result
	@api.multi
	def write(self, values):
		result = super(consumtion_fuel_log_model, self).write(values)
		if self.card_name and self.liter:
			consumed_liter_fuel = self.liter
			remaining_fuel = self.card_name.card_limit_remaining - consumed_liter_fuel
			self.card_name.card_limit_remaining = remaining_fuel
		return result