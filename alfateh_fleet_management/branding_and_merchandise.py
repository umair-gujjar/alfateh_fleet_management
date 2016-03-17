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



#class select_assesment_list(models.Model):
	#_name = 'select_assesment_list'
	#name = fields.Many2one('assesment_list','Select Assesment List')
	#assesmnet_date = fields.Date('Date')
	#company_name = fields.Char('Company Name')
	#department = fields.Char('Department')
	#sa_num = fields.Char('SA #')
	#select_assesment_list_id = fields.One2many('select_assesment_list_fields','select_assesment_list_fields_id')
	#@api.multi
	#def action_create_assesment_list(self):
		#self.select_assesment_list_id = self._prepare_assesment_list_lines(self.name)
		#return True
	#@api.multi
	#def _prepare_assesment_list_lines(self, check, force_fill=False):
		#new_data = []
		#for line in check.check_list_id:
			#data = self._prepare_assesment_list_line(check, line, fill=force_fill)
			#new_data.append((0, 0, data))
		#return new_data
	#@api.multi
	#def _prepare_assesment_list_line(self, check, line, fill=None):
		#data = {
			#'assesment_check': line.assesment_check,
			#'factor': line.factor,
			#'grade': line.grade,
		#}
		#return data

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

	




