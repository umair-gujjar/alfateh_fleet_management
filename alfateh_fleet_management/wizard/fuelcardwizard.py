from openerp.osv import fields, osv
from openerp.tools.translate import _
class validate_account_move_lines(osv.osv_memory):
    _name = "fuelcardwizard.fuel_card_management"
    _description = "Recharge Fuel Cards"

    def dos_recalculate_amount(self, cr, uid, ids, context=None):
        obj_move_line = self.pool.get('fuelcard.management')
        move_ids = []
        if context is None:
            context = {}
        data_line = obj_move_line.browse(cr, uid, context['active_ids'], context)
        for line in data_line:
            line.card_limit_remaining = line.card_limit

            print "Code **************************"
        return {'type': 'ir.actions.act_window_close'}