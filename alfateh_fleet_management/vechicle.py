from openerp import models, fields, api
import datetime
from datetime import date, datetime
import time

class alfateh_fleet_management(models.Model):
	_inherit = 'fleet.vehicle'
	engine_num = fields.Char('Engine Num')
	average_consumption = fields.Float('Average Consumption')
	expiry_token = fields.Date('Expiry Token')
	capacity = fields.Char('capacity')
	vehicle_status = fields.Char('vehicle status')



class alfateh_vehicle_cost(models.Model):
	_inherit = 'fleet.vehicle.cost'
	vehicle_trip = fields.Many2one('trip.management', string="Trip")
	


