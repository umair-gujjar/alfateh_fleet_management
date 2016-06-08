from openerp import models, fields, api
class Wizard(models.TransientModel):
    _name = 'clearlimitwizard.fleet_vehicle'
    _description = "Compute Repair checkbox"
    @api.multi
    def dos_recompute_chkbox(self):
        obj_move_line = self.env['fleet.vehicle'].browse(self._context.get('active_ids'))
        for line in obj_move_line:
            if line.odometer > line.gear_oil_value:
                line.gear_oil_chk_box = True
            else:
                line.gear_oil_chk_box = False    
            if line.odometer > line.air_filter_value:
                line.air_filter_chk_box = True
            else:
                line.air_filter_chk_box = False    
            if line.odometer > line.oil_filter_value:
                line.oil_filter_chk_box = True
            else:
                line.oil_filter_chk_box = False    
            if line.odometer > line.engine_oil_change_value:
                line.engine_oil_chk_box = True
            else:
                line.engine_oil_chk_box = False

        return True        