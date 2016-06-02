from openerp import models, fields, api

class check_list(models.Model):
	_name = 'check_list'
	name = fields.Char('Name')
	check_list_id= fields.One2many('check_list_fields','check_list_fields_id')



class check_list_fields(models.Model):
	_name = 'check_list_fields'
	name = fields.Char('Name')
	daily_vehicle_check = fields.Char('Name')
	status_yes = fields.Boolean('Yes')
	status_no = fields.Boolean('No')
	descp_of_defect = fields.Char('Description of Defect')
	defect_corrected = fields.Char('Defect Corrected')
	check_list_fields_id = fields.Many2one('check_list','Check List')


class select_check_list(models.Model):
	_name = 'select_check_list'
	name = fields.Many2one('check_list','Daily Check List')
	list_date = fields.Date('Date')
	Vehicle_id = fields.Many2one('fleet.vehicle','Vehicle')
	vehicle_type = fields.Char('Vehicle Type')
	vehicle_meter_reading = fields.Char('Meter Reading')
	select_check_list_id = fields.One2many('select_check_list_fields','select_check_list_fields_id')
	@api.multi
	def action_create_check_list(self):
		self.select_check_list_id = self._prepare_check_list_lines(self.name)
		return True
	@api.multi
	def _prepare_check_list_lines(self, check, force_fill=False):
		new_data = []
		for line in check.check_list_id:
			data = self._prepare_check_list_line(check, line, fill=force_fill)
			new_data.append((0, 0, data))
		return new_data
	@api.multi
	def _prepare_check_list_line(self, check, line, fill=None):
		data = {
			'daily_vehicle_check': line.daily_vehicle_check,
			'status_yes': line.status_yes,
			'status_no': line.status_no,
			'descp_of_defect': line.descp_of_defect,
			'defect_corrected': line.defect_corrected,
		}
		return data

class select_check_list_fields(models.Model):
	_name = 'select_check_list_fields'
	name = fields.Char('Name')
	daily_vehicle_check = fields.Char('Name')
	status_yes = fields.Boolean('Yes')
	status_no = fields.Boolean('No')
	descp_of_defect = fields.Char('Description of Defect')
	defect_corrected = fields.Char('Defect Corrected')
	select_check_list_fields_id = fields.Many2one('select_check_list','Check List')