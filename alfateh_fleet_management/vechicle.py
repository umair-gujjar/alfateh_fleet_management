from openerp import models, fields, api

class alfateh_fleet_management(models.Model):
	_inherit = 'fleet.vehicle'
	engine_num = fields.Char('Engine Num')
	average_consumption = fields.Float('Average Consumption')
	expiry_token = fields.Date('Expiry Token')
	capacity = fields.Char('capacity')
	vehicle_status = fields.Char('vehicle status')



class alfateh_vehicle_cost(models.Model):
	_inherit = 'fleet.vehicle.cost'
	trip = fields.Many2one('res.partner', string="Trip", domain="[('is_company','=',True)]")
	


