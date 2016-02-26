# -*- coding: utf-8 -*-

import datetime
from datetime import date, datetime
import time
from openerp import models, fields, api



class maintaince_checklist(models.Model):
	_name = 'vehical_maintaince_checklist'
	checklist_date = fields.Date('Date', required=True)
	checklist_vehicle = fields.Many2one('fleet.vehicle','Vehicle',required=True)
	checklost_meter =  fields.Float("Meter Reading")
	checklist_vehicle_type = fields.Char('Vehicle Type',required=True)
	checklist_engine_oil_yes = fields.Boolean("Yes")
	checklist_engine_oil_no = fields.Boolean("No")
	checklist_fluid_level_yes = fields.Boolean("Yes")
	checklist_fluid_level_no = fields.Boolean("No")
	checklist_seat_belt_yes = fields.Boolean("Yes")
	checklist_seat_belt_no = fields.Boolean("No")
	checklist_fog_light_yes = fields.Boolean("Yes")
	checklist_fog_light_no = fields.Boolean("No")
	checklist_door_lock_yes = fields.Boolean("Yes")
	checklist_door_lock_no = fields.Boolean("No")
	checklist_gear_oil_yes = fields.Boolean("Yes")
	checklist_gear_oil_no = fields.Boolean("No")
	checklist_steering_oil_yes = fields.Boolean("Yes")
	checklist_steering_oil_no = fields.Boolean("No")
	checklist_brake_lines_yes = fields.Boolean("Yes")
	checklist_brake_lines_no = fields.Boolean("No")
	checklist_brake_operation_yes = fields.Boolean("Yes")
	checklist_brake_operation_no = fields.Boolean("No")
	checklist_wiper_blade_yes = fields.Boolean("Yes")
	checklist_wiper_blade_no = fields.Boolean("No")
	checklist_head_light_yes = fields.Boolean("Yes")
	checklist_head_light_no = fields.Boolean("No")
	checklist_power_steer_yes = fields.Boolean("Yes")
	checklist_power_steer_no = fields.Boolean("No")
	checklist_exhaust_system_yes = fields.Boolean("Yes")
	checklist_exhaust_system_no = fields.Boolean("No")
	checklist_parking_brake_yes = fields.Boolean("Yes")
	checklist_parking_brake_no = fields.Boolean("No")
	checklist_fan_belt_yes = fields.Boolean("Yes")
	checklist_fan_belt_no = fields.Boolean("No")
	checklist_mirror_yes = fields.Boolean("Yes")
	checklist_mirror_no = fields.Boolean("No")
	checklist_break_light_yes = fields.Boolean("Yes")
	checklist_break_light_no = fields.Boolean("No")
	checklist_break_flight_yes = fields.Boolean("Yes")
	checklist_break_flight_no = fields.Boolean("No")
	checklist_tail_light_yes = fields.Boolean("Yes")
	checklist_tail_light_no = fields.Boolean("No")
	checklist_power_steering_fluid_yes = fields.Boolean("Yes")
	checklist_power_steering_fluid_no = fields.Boolean("No")
	checklist_tire_inflation_yes = fields.Boolean("Yes")
	checklist_tire_inflation_no = fields.Boolean("No")
	checklist_water_screenwash_yes = fields.Boolean("Yes")
	checklist_water_screenwash_no = fields.Boolean("No")
	checklist_tire_balance_yes = fields.Boolean("Yes")
	checklist_tire_balance_no = fields.Boolean("No")
	checklist_spare_tire_yes = fields.Boolean("Yes")
	checklist_spare_tire_no = fields.Boolean("No")
	checklist_horn_yes = fields.Boolean("Yes")
	checklist_horn_no = fields.Boolean("No")
	checklist_chocks_yes = fields.Boolean("Yes")
	checklist_chocks_no = fields.Boolean("No")
	checklist_indicator_yes = fields.Boolean("Yes")
	checklist_indicator_no = fields.Boolean("No")
	checklist_battery_yes = fields.Boolean("Yes")
	checklist_battery_no = fields.Boolean("No")
	checklist_number_plate_yes = fields.Boolean("Yes")
	checklist_number_plate_no = fields.Boolean("No")
	checklist_reflector_yes = fields.Boolean("Yes")
	checklist_reflector_no = fields.Boolean("No")
	checklist_inner_wall_yes = fields.Boolean("Yes")
	checklist_inner_wall_no = fields.Boolean("No")
	checklist_outer_wall_yes = fields.Boolean("Yes")
	checklist_outer_wall_no = fields.Boolean("No")
	checklist_floor_yes = fields.Boolean("Yes")
	checklist_floor_no = fields.Boolean("No")
	checklist_load_yes = fields.Boolean("Yes")
	checklist_load_no = fields.Boolean("No")
	checklist_breakout_kit_yes = fields.Boolean("Yes")
	checklist_breakout_kit_no = fields.Boolean("No")
	checklist_wiper_yes = fields.Boolean("Yes")
	checklist_wiper_no = fields.Boolean("No")
	checklist_driver_lic_yes = fields.Boolean("Yes")
	checklist_driver_lic_no = fields.Boolean("No")







	_defaults = {
    'checklist_date': datetime.now(),
    }
	
