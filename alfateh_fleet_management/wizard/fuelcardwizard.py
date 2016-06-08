from openerp import models, fields, api
class Wizard(models.TransientModel):
    _name = 'fuelcardwizard.fuel_card_management'
    _description = "Recharge Fuel Cards"
    @api.multi
    def dos_recalculate_amount(self):
        obj_move_line = self.env['fuelcard.management'].browse(self._context.get('active_ids'))
        for line in obj_move_line:
            recharge_amount = line.card_limit - line.card_limit_remaining
            line.card_limit_remaining = line.card_limit - recharge_amount
            recharge_records = self.env['recharge']
            res = {
            'name': line.id,
            'card_recharge_liter': recharge_amount,
            }
            recharge_records.create(res)