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
	#company_name = fields.Char('Name of Company')
	company_name = fields.Many2one('res.partner','Name of Company',required=True)
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
		('no', 'No')], string="previous Contract with our Company(if Any)")


	state = fields.Selection([('application', 'Application'),
		('assesment', 'Assessment'),
		('finished', 'Done'),],default='application')


	@api.onchange('company_name')
	def onchange_route_field(self):
		self.ntn_num = self.company_name.x_ntn_num
		self.stn_num = self.company_name.x_stn_num
		self.website = self.company_name.website
		self.company_type = self.company_name.x_company_type
		print self.company_name.name


	@api.multi
	def concept_progressbar(self):
		self.ensure_one()
		self.write({
			'state': 'assesment',
			})

	@api.multi
	def started_progressbar(self):
		self.ensure_one()
		self.write({
			'state': 'started'
			})

	@api.multi
	def progress_progressbar(self):
		self.ensure_one()
		self.write({
			'state': 'progress'
			})

	@api.multi
	def done_progressbar(self):
		self.ensure_one()
		self.write({
			'state': 'finished',
			})

	




