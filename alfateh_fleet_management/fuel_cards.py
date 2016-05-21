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
	card_consume_h_ids = fields.One2many('consumehistory','card_consume_h_id',string='Details')
	card_recharge_h_ids = fields.One2many('rechargehistory','card_recharge_h_id',string='Details')
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

	#@api.one
	#def recharge(self):
	#	if self.card_limit and self.card_limit_remaining:
	#		recharageable_ltrs = self.card_limit - self.card_limit_remaining
	#		if self.card_limit_remaining < self.card_limit:
	#			self.card_limit_remaining = self.card_limit_remaining + recharageable_ltrs
	#		else:
	#			self.card_limit_remaining = self.card_limit_remaining
#for consume history 
	@api.multi
	def update_consume_history(self):
		self.card_consume_h_ids.unlink()
		self.card_consume_h_ids = self._prepare_mo_workbook_one_ids()

	@api.multi
	def _prepare_mo_workbook_one_ids(self):
		new_data = []
		all_recd_consume = self.env['consume'].search([('name','=',self.id)])
		all_recd = self.env['consume'].search([])
		print all_recd_consume
		print all_recd
		for line in all_recd_consume:
			data = self._prepare_workbook_one_line(line)
			new_data.append(data)
		return new_data
	@api.multi
	def _prepare_workbook_one_line(self, data):
		data = {
		'card_consume_date': data.card_consume_date,
		'card_consume_liter': data.card_consume_liter,
			}
		return data
#for recharge history
	@api.multi
	def update_recharge_history(self):
		self.card_recharge_h_ids.unlink()
		self.card_recharge_h_ids = self._prepare_workbook_one_ids()

	@api.multi
	def _prepare_workbook_one_ids(self):
		new_data = []
		all_recd_recharge = self.env['recharge'].search([('name','=',self.id)])
		for line in all_recd_recharge:
			data = self._prepare_workbook_one_lines(line)
			new_data.append(data)
		return new_data
	@api.multi
	def _prepare_workbook_one_lines(self, data):
		data = {
		'card_recharge_date': data.card_recharge_date,
		'card_recharge_liter': data.card_recharge_liter,
			}
		return data
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
	fuel_type = fields.Selection([('fuel_gasoline_rate', 'Gasoline'), ('fuel_disel_rate', 'Diesel'), ('fuel_hioctane_rate', 'Hi-Octane'), ('fuel_cng_rate', 'CNG')], 'Fuel Type',select=True, help='Fuel Used by the vehicle')
	fuel_amount = fields.Float('Fuel Amount')


	_defaults = {
	'card_recharge_date': datetime.now(),
	}

	@api.onchange('fuel_type','card_recharge_liter')
	def onchange_atfc_atoc_field(self):
		fuel_rate_rec = self.env['fuel.rate']
		if self.fuel_type and self.card_recharge_liter:
			if self.fuel_type == 'fuel_gasoline_rate':
				self.fuel_amount = fuel_rate_rec.search([]).fuel_gasoline_rate * self.card_recharge_liter
			elif self.fuel_type == 'fuel_hioctane_rate':
				self.fuel_amount = fuel_rate_rec.search([]).fuel_hioctane_rate * self.card_recharge_liter
			elif self.fuel_type == 'fuel_cng_rate':
				self.fuel_amount = fuel_rate_rec.search([]).fuel_cng_rate * self.card_recharge_liter
			else:
				self.fuel_amount = fuel_rate_rec.search([]).fuel_disel_rate * self.card_recharge_liter

	@api.model
	def create(self, vals):
		result = super(recharge, self).create(vals)
		recharge_liter_fuel = vals['card_recharge_liter']
		fuel_management_card = self.env['fuelcard.management'].search([('id','=', vals.get('name'))])
		remaining_fuel = fuel_management_card.card_limit_remaining + recharge_liter_fuel
		fuel_management_card.card_limit_remaining = remaining_fuel
		return result
	@api.multi
	def write(self, values):
		result = super(recharge, self).write(values)
		if self.name and self.card_recharge_liter:
			recharge_liter_fuel = self.card_recharge_liter
			remaining_fuel = self.card_name.card_limit_remaining + recharge_liter_fuel
			self.card_name.card_limit_remaining = remaining_fuel
		return result


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

class consumehistory(models.Model):
	_name = 'consumehistory'
	card_consume_date = fields.Date('Date')
	card_consume_liter = fields.Float('Consume liters')
	card_consume_h_id = fields.Many2one('fuelcard.management',string='Consume')

class rechargehistory(models.Model):
	_name = 'rechargehistory'
	card_recharge_date = fields.Date('Date')
	card_recharge_liter = fields.Float('Recharge liters')
	card_recharge_h_id = fields.Many2one('fuelcard.management',string='Recharge')