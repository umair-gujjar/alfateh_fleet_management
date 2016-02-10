# -*- coding: utf-8 -*-

from openerp import models, fields, api
import datetime
from datetime import date, datetime
import time



# Route Management
class route_driver(models.Model):
	_inherit = 'res.partner'
	driver_lic_num = fields.Char('Licence Number')
	driver_cnic_num = fields.Char('CNIC Number')
	driver_employee_id = fields.Char('Employee ID')
	driver_dob = fields.Date('D.O.B')
	driver_age = fields.Float('Age(years)')

	_defaults = {
    'customer': False,
    }

	@api.onchange('driver_dob')
	def do_stuff(self):
		d_dob = self.driver_dob
		if d_dob:
			age = datetime.now().date() - datetime.strptime(self.driver_dob, '%Y-%m-%d').date()
			days = age.days
 			months = days/30.43
 			years = days/365
 			self.driver_age= years 
	
	
				
				
	