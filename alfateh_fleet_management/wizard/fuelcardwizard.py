from openerp import models, fields, api
class Wizard(models.TransientModel):
    _name = 'fuelcardwizard.fuel_card_management'
    _description = "Recharge Fuel Cards"
    @api.multi
    def dos_recalculate_amount(self):
        obj_move_line = self.env['fuelcard.management'].browse(self._context.get('active_ids'))
        for line in obj_move_line:
            gas = None
            recharge_amount = line.card_limit - line.card_limit_remaining
            line.card_limit_remaining = line.card_limit - recharge_amount
            recharge_records = self.env['recharge']
            fuel_rate_rec = self.env['fuel.rate'].search([])
            if line.fuel_type == 'fuel_gasoline_rate':
                if fuel_rate_rec.search([]).fuel_gasoline_rate == 0:
                    raise Warning('Gasoline Rate is Zero it cannot get the amount Please Change its value in Fuel Rates !')
                else:
                    gas = recharge_amount / fuel_rate_rec.fuel_gasoline_rate
            elif line.fuel_type == 'fuel_hioctane_rate':
                if fuel_rate_rec.search([]).fuel_hioctane_rate == 0:
                    raise Warning('Gasoline Rate is Zero it cannot get the amount Please Change its value in Fuel Rates !')
                else:
                    gas = recharge_amount / fuel_rate_rec.fuel_hioctane_rate
            elif line.fuel_type == 'fuel_cng_rate':
                if fuel_rate_rec.search([]).fuel_cng_rate == 0:
                    raise Warning('Gasoline Rate is Zero it cannot get the amount Please Change its value in Fuel Rates !')
                else:
                    gas = recharge_amount / fuel_rate_rec.fuel_cng_rate
            else:
                if fuel_rate_rec.search([]).fuel_disel_rate == 0:
                    raise Warning('Gasoline Rate is Zero it cannot get the amount Please Change its value in Fuel Rates !')
                else:
                    gas = recharge_amount / fuel_rate_rec.fuel_disel_rate
            res = {
            'name': line.id,
            'card_recharge_liter': recharge_amount,
            'fuel_type' : line.fuel_type,
            'fuel_amount' : gas,
            }
            recharge_records.create(res)