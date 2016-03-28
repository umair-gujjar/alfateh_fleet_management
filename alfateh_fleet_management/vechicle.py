from openerp import models, fields, api
import datetime
from datetime import date, datetime
import time

class alfateh_fleet_management(models.Model):
	_inherit = 'fleet.vehicle'
	engine_num = fields.Char('Engine Num')
	average_consumption = fields.Float('Average Consumption')
	expiry_token = fields.Date('Expiry Token')
	capacity = fields.Char('Capacity')
	vehicle_status = fields.Char('Vehicle Status')
	vehicle_type_fleet = fields.Selection([
            ('Bus', 'Bus'),
            ('Truck', 'Truck'),
            ('Car', 'Car'),
            ('Auto_Rickshaw', 'Auto Rickshaw'),
            ('Van', 'Van'),
            ],default='', string="Select Vehicle Type",)


class alfateh_vehicle_cost(models.Model):
	_inherit = 'fleet.vehicle.cost'
	vehicle_trip = fields.Many2one('trip.management', string="Trip" ,domain="[('date','=',date)]")


class fuel_log(models.Model):
	_inherit = 'fleet.vehicle.log.fuel'
	card_name = fields.Many2one('fuelcard.management',string='Card Name')

	@api.onchange('card_name')
	def testing_lter_change(self):
		print self.card_name
	
	


