# -*- coding: utf-8 -*-

from openerp import models, fields, api
import datetime
from datetime import date, datetime
import time
from openerp.exceptions import ValidationError

class edit_company(models.Model):
	_inherit = 'res.partner'
	x_ntn_num = fields.Char('NTN # ')
	x_stn_num = fields.Char('STN #')
	x_company_type =  fields.Selection([('single_member_company', 'Single Member Company'),
		('private', 'Private Company'),
		('public_listed_company', 'Public Listed Company'),
		('public_unlisted_company', 'Public Unlisted Company'),
		('any_other_company', 'Any other company')], string="Type of Company")

class custom_contract(models.Model):
	_inherit = 'hr.contract'
	x_purchase_amount = fields.Char('Purchase Amount')
	x_purchase_qty = fields.Char('Purchase Qty')
	x_sale_target = fields.Char('Sale Target')
	x_select_cb = fields.Selection([
		('cash', 'Cash'),
		('bank','Bank')], string="Type")

	wrkbk_cash_ids = fields.One2many('workbook_for_cash','wrkbk_for_cash')
	wrkbk_bank_ids = fields.One2many('workbook_for_bank','wrkbk_for_bank')
	wrkbk_summary_ids = fields.One2many('summary_alfateh_workbook','alf_workbook_id')
	



class branding_merchandise(models.Model):
	_name = 'branding.management'
	_inherit = ['mail.thread', 'ir.needaction_mixin']
	name = fields.Char('Name')
	bmaf = fields.Char('BMAF #')
	saf = fields.Char('SAF #')
	cnic_num = fields.Char('CNIC #')
	cell_num = fields.Char('Cell #')
	designation = fields.Char('Designation')
	email_address = fields.Char('Email Address')	
	representative_name = fields.Char('Name of Representative')
	name_of_company= fields.Many2one('res.partner','Name of Company',required=True)
	registered_address = fields.Char('Registered Address')
	website = fields.Char('Website ')
	ntn_num = fields.Char('NTN # ')
	stn_num = fields.Char('STN #')
	contract_duration = fields.Char('Contract Period Required')
	contract_start_date = fields.Date('Start Date')
	contract_end_date = fields.Date('End Date')
	contract_num = fields.Char('Contract/Agreement #')
	List_outlet = fields.Char('List of Outlet and Space Required')
	num_of_outlets = fields.Integer('No. of Outlets Required')
	outlet_details = fields.Char('Outlet Detail')
	department_details = fields.Char('Department Detail')
	company_type =  fields.Char()
	previous_contract =  fields.Selection([('yes', 'Yes'),
		('no', 'No')], string="Previous Contract with our Company(if Any)")
	assesment_list_name = fields.Many2one('assesment_list','Select Assesment List')
	assesmnet_date = fields.Date('Date')
	company_name = fields.Char('Company Name')
	department = fields.Char('Department')
	sa_num = fields.Char('SA #')
	total_marks = fields.Char('Total Points')
	select_assesment_list_id = fields.One2many('select_assesment_list_fields','select_assesment_list_fields_id')

	@api.multi
	def action_calculate_mark(self):
		#self.total_marks = self._prepare_assesment_list_lines(self.assesment_list_name)
		#return True\
		total_calculated_marks = 0 
		for grade in self.select_assesment_list_id:
			total_calculated_marks = total_calculated_marks +  (float(grade.grade) * grade.factor)
			print total_calculated_marks

		self.total_marks = total_calculated_marks	



	@api.multi
	def action_create_assesment_list(self):
		self.select_assesment_list_id = self._prepare_assesment_list_lines(self.assesment_list_name)
		return True
	@api.multi
	def _prepare_assesment_list_lines(self, assesment, force_fill=False):
		new_data = []
		for line in assesment.assesment_list_id:
			data = self._prepare_assesment_list_line(assesment, line, fill=force_fill)
			new_data.append((0, 0, data))
		return new_data
	@api.multi
	def _prepare_assesment_list_line(self, assesment, line, fill=None):
		data = {
			'assesment_check': line.assesment_check,
			'factor': line.factor,
			'grade': line.grade,
		}
		return data


	state = fields.Selection([('application', 'Application'),
		('assesment', 'Assessment'),],default='application')


	@api.onchange('name_of_company')
	def onchange_assesment_form_field(self):
		self.ntn_num = self.name_of_company.x_ntn_num
		self.stn_num = self.name_of_company.x_stn_num
		self.website = self.name_of_company.website
		self.company_type = self.name_of_company.x_company_type
		self.company_name = self.name_of_company.name
		print self.name_of_company.name


	@api.multi
	def go_to_assesment(self):
		self.ensure_one()
		self.write({
			'state': 'assesment',
			})

	@api.multi
	def go_to_application(self):
		self.ensure_one()
		self.write({
			'state': 'application'
			})

	@api.multi
	def create_contract(self):
		#print self.name_of_company.name
		resee =self.env['hr.employee'].create({'name':self.name_of_company.name})
		resee.partner_id = self.name_of_company

		print 'xxxxx------'+str(resee.name)
		
		return {
            'name': 'Contract Form',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'hr.contract',
            'type': 'ir.actions.act_window',
            'context': "{'employee_id': '%s'}" % (resee.id),
        }


class assesment_list(models.Model):
	_name = 'assesment_list'
	name = fields.Char('Name')
	assesment_list_id= fields.One2many('assesment_list_fields','assesment_list_fields_id')



class assesment_list_fields(models.Model):
	_name = 'assesment_list_fields'
	name = fields.Char('Name')
	assesment_check = fields.Char('Name')
	factor = fields.Float('Factor')
	grade =  fields.Selection([('1', 'Poor/No'),
		('2', 'Average'),
		('3', 'Good'),
		('4', 'Excellent/Yes')], string="Grade")
	
	assesment_list_fields_id = fields.Many2one('assesment_list','Check List')

class select_assesment_list_fields(models.Model):
	_name = 'select_assesment_list_fields'
	name = fields.Char('Name')
	assesment_check = fields.Char('Name')
	factor = fields.Float('Factor')
	grade =  fields.Selection([('1', 'Poor/No'),
		('2', 'Average'),
		('3', 'Good'),
		('4', 'Excellent/Yes')], string="Grade")
	select_assesment_list_fields_id = fields.Many2one('branding.management','Check List')

class purchase_qutoation_taxtech(models.Model):
    _inherit = "hr.employee"
    partner_id = fields.Many2one('res.partner','Related Partner')


class workbook_cash(models.Model):
	_name = 'workbook_for_cash'
	cash_location = fields.Char(string='Location')
	cash_amount = fields.Float(string='Amount')
	cash_date = fields.Char(string='Date')
	
	wrkbk_for_cash = fields.Many2one('hr.contract','Work cash Id')    

class workbook_bank(models.Model):
	_name = 'workbook_for_bank'
	bank_location = fields.Char(string='Location')
	bank_amount = fields.Float(string='Amount')
	bank_date = fields.Char(string='Date')
	bank_tax_section = fields.Char(string='Tax Section')
	wrkbk_for_bank = fields.Many2one('hr.contract','Work bank Id')  


	
# hr_ class inherit
class alfateh_hr_payslip_custom(models.Model):
	_inherit = 'hr.payslip'

	@api.multi
	def confirm_custom_entry(self):
		if self.move_id:
			recs = self.move_id.line_id
			emp_partner_id = self.env['res.partner'].search([('name','=',self.employee_id.name)])
			for item in recs:
				item.partner_id = emp_partner_id.id
	@api.multi
	def write(self, move_id):
		res = super(alfateh_hr_payslip_custom, self).write(move_id)
		if self.move_id:
			recs = self.move_id.line_id
			#by name search we get employee partner name
			#emp_partner_id = self.env['res.partner'].search([('name','=',self.employee_id.name)])
			for item in recs:
			#	item.partner_id = emp_partner_id.id

			# by getting partner id from employee id we fetch partner name
				item.partner_id = self.employee_id.partner_id.id

		return res



class contract_summary_alfateh_workbook(models.Model):
	_name = 'summary_alfateh_workbook'
	location = fields.Char(string='Location')
	ntn_number = fields.Char(string='NTN')
	date_from = fields.Date(string='From')
	date_to  = fields.Date(string='To')
	area_space = fields.Char(string='Area/Space')
	no_of_amount = fields.Float(string='Amount')
	alf_workbook_id = fields.Many2one('hr.contract','Work Book Id')