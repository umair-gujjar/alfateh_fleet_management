from openerp.osv import osv,fields
from datetime import date, datetime
class outwardpass(osv.Model):
	_name='outwardpass'
	_inherit = ['mail.thread', 'ir.needaction_mixin']
	_columns= {
	'name': fields.char('Name',readonly=True),
	'date' : fields.date('Date', ),
	'invoice_ref' : fields.char('Invoice Ref #', size=32),
	'gin' : fields.char('GIN #',size=32 ),
	'bilty' : fields.char('Bilty ',size=32),
	'time_out' : fields.datetime('Time Out', ),
	'vehicle' : fields.char('Vehicle',size=32),
	'time_in' : fields.datetime('Time In',  ),
	'vehicle_type' : fields.char('Vehicle Type',size=32),
	'supplier_details': fields.many2one('res.partner','Supplier'),
	'in_inward_id' : fields.one2many('in_outward','in_outwardpass_id',string='Details'),
	'out_inward_id' : fields.one2many('out_outward','out_outwardpass_id',string='Details'),
	'in_remarks' : fields.text('Remarks'),
	'out_remarks' : fields.text('Remarks'),
	'srin' : fields.char('SRIN #',size=32),
	'branch' : fields.many2one('stock.location','Branch Name'),
	'gi_seal': fields.char('Seal In'),
	'go_seal': fields.char('Seal Out'),
	'vehicle_num' : fields.char('Vehicle Number',size=32),
	'fleet_vehicle_id' : fields.many2one('fleet.vehicle','Vehicle'),
	'time_duration' : fields.float('Time Duration'),
	'out_driver' : fields.many2one('res.partner','Driver',domain="['|',('customer','!=',True),('employee','=',True)]"),
	'out_date' : fields.date('Date', ),
	'out_nature' : fields.boolean('Return or Rejection'),
	'out_gon' : fields.char('GON #',),
	'out_sron' : fields.char('SRON #',size=32),
	'out_time_out' : fields.datetime('Time Out',),
	'out_vehicle' : fields.char('Vehicle',size=32),
	'out_supplier_details': fields.many2one('res.partner','Supplier Details'),
	'out_document_ref' : fields.char('Document Ref #',size=32),
	'out_remarks' : fields.text('Remarks'),
	'trip_management_field': fields.many2one('trip.management','Trip'),
	'gp_odoo_meter': fields.float("Odoo Meter Exit"),
	'gpi_odoo_meter': fields.float("Odoo Meter Enterance"),
	'odoometer_difference' : fields.float('Odoo Meter Difference'),
	'out_reference_field': fields.char('Reference', size=64),
	'out_time_in' : fields.datetime('Time In',),
	'out_dept': fields.char('Department/Section', size=32),
	'out_stock_location_id' : fields.many2one('stock.location','Dept'),
	'in_inret_id' : fields.one2many('in_inret','in_inwardret_id',string='Details'),
	'out_inret_id' : fields.one2many('out_inret','out_inwardret_id',string='Details'),
	'in_inshop_id' : fields.one2many('in_inshop','in_inwardshop_id',string='Details'),
	'out_inshop_id' : fields.one2many('out_inshop','out_inwardshop_id',string='Details'),
	'select_sequence' : fields.many2one('ir.sequence','Select Category',required=True,help="Please select the sequence."),
	'workers': fields.char('No of Workers',size=32),
	'transfer_order': fields.char('Transfer Order',size=32),
	'driver_text': fields.char('Driver',size=32),
	'rep_rec_no': fields.char('Repair Requisition No',size=32),
	'lc_pc' : fields.selection([
            ('lc', 'LC'),
            ('pc', 'PO'),
            ],default='', string="LC or PO"),

	'vehicle_type_fleet' : fields.selection([
            ('Bus', 'Bus'),
            ('Truck', 'Truck'),
            ('Car', 'Car'),
            ('Auto_Rickshaw', 'Auto Rickshaw'),
            ('Van', 'Van'),
            ],default='', string="Select Vehicle Type",),
	'outward_Category' : fields.selection([
            ('Shop', 'Shop'),
            ('Market_Purchase', 'Market Purchase'),
            ('General', 'General'),
            ('Returnable', 'Returnable'),
            ],default='', string="Select the Category"),
	'lc_pc_ref' : fields.char('LC or PO Ref #',size=32),
	
    'state' : fields.selection([
            ('vehicle_enter', 'Gate Out'),
            ('vehicle_process', 'Gate In'),
            ('vehicle_exit', 'Complete'),
            ],default='vehicle_enter'),
    'own_vehicle' : fields.boolean('Rented Vehicle'),
	}

	def create(self, cr, uid, vals, context=None):
		sequence=self.pool.get('ir.sequence').get(cr, uid, 'outwardpass')
		seq_out_gon_shop = self.pool.get('ir.sequence').get(cr, uid, 'Shopoutpass')
		vals['name']="Out_"+vals['outward_Category']+"_"+sequence
		vals['out_gon'] = "Outward-"+vals['outward_Category']+"-"+seq_out_gon_shop

		return super(outwardpass, self).create(cr, uid, vals, context=context)
	_defaults = {
				'gin': lambda obj, cr, uid, context: '/',
				'out_gon': lambda obj, cr, uid, context: '/',

				'time_out': lambda obj, cr, uid, context: datetime.now(),
				'time_in': lambda obj, cr, uid, context: datetime.now(),
				'out_date': lambda obj, cr, uid, context: datetime.now(),
				'out_time_out': lambda obj, cr, uid, context: datetime.now(),
				'date': lambda obj, cr, uid, context: datetime.now(),
				'out_time_out': lambda obj, cr, uid, context: datetime.now(),
				'out_time_in': lambda obj, cr, uid, context: datetime.now(),
	 }		

class in_inward(osv.Model):
    _name = 'in_outward'
    _columns= {
    'uom': fields.char('UOM'),
    'qty': fields.char('QTY'),
    'item': fields.char('Item Category'),
    'in_outwardpass_id' : fields.many2one('outwardpass','Item Category'),
    }

class out_inward(osv.Model):
    _name = 'out_outward'
    _columns= {
    'uom': fields.char('UOM'),
    'qty': fields.char('QTY'),
    'item': fields.char('Item Category'),
    'out_outwardpass_id' : fields.many2one('outwardpass','Item Category'),
    }


class inwardpass(osv.Model):
	_name='inwardpass'
	_inherit = ['mail.thread', 'ir.needaction_mixin']
	_columns= {
	'name': fields.char('Name',readonly=True),
	'date' : fields.date('Date', ),
	#'document_type' : fields.boolean('LC or PO'),
	'invoice_ref' : fields.char('Invoice Ref #', size=32),
	'gin' : fields.char('GIN #',size=32 ),
	#'lc' : fields.char('LC Ref.#/PO #',size=32),
	'bilty' : fields.char('Bilty ',size=32),
	'time_out' : fields.datetime('Time Out', ),
	'vehicle' : fields.char('Vehicle',size=32),
	'time_in' : fields.datetime('Time In',  ),
	'vehicle_type' : fields.char('Vehicle Type',size=32),
	'supplier_details': fields.many2one('res.partner','Supplier '),
	'in_inward_id' : fields.one2many('in_inward','in_inwardpass_id',string='Details'),
	'out_inward_id' : fields.one2many('out_inward','out_inwardpass_id',string='Details'),
	'in_remarks' : fields.text('Remarks'),
	'out_remarks' : fields.text('Remarks'),
	'gi_seal': fields.char('Seal In'),
	'go_seal': fields.char('Seal Out'),
	'vehicle_num' : fields.char('Vehicle Number',size=32),
	'fleet_vehicle_id' : fields.many2one('fleet.vehicle','Vehicle'),
	'time_duration' : fields.float('Time Duration'),
	'out_driver' : fields.many2one('res.partner','Driver',domain="['|',('customer','!=',True),('employee','=',True)]"),
	'out_date' : fields.date('Date', ),
	'out_nature' : fields.boolean('Return or Rejection'),
	'out_gon' : fields.char('GON #',),
	'workers': fields.char('No of Workers',size=32),
	'out_time_in' : fields.datetime('Time In',),
	'out_sron' : fields.char('SRON Ref.',size=32),
	'out_time_out' : fields.datetime('Time Out',),
	'out_vehicle' : fields.char('Vehicle',size=32),
	'out_supplier_details': fields.many2one('res.partner','Supplier Details'),
	'out_remarks' : fields.text('Remarks'),
	'trip_management_field': fields.many2one('trip.management','Trip'),
	'gp_odoo_meter': fields.float("Odoo Meter Exit"),
	'out_dept': fields.char('Department/Section', size=32),
	'gpi_odoo_meter': fields.float("Odoo Meter Enterance"),
	'odoometer_difference' : fields.float('Odoo Meter Difference'),
	'in_outret_id' : fields.one2many('in_outret','in_outwardret_id',string='Details'),
	'out_outret_id' : fields.one2many('out_outret','out_outwardret_id',string='Details'),
	'out_stock_location_id' : fields.many2one('stock.location','Dept'),
	'out_document_ref' : fields.char('Document Ref #',size=32),
	'select_sequence' : fields.many2one('ir.sequence','Select Category',required=True,help="Please select the sequence."),
	'rep_rec_no': fields.char('Repair Requisition No',size=32),
	'lc_pc' : fields.selection([
            ('lc', 'LC'),
            ('pc', 'PO'),
            ],default='', string="LC or PO"),
	'lc_pc_ref' : fields.char('LC or PO Ref #',size=32),

	'inward_Category' : fields.selection([
            ('supplier', 'Supplier'),
            ('general', 'General'),
            ('returnable', 'Returnable'),
            ],default='', string="Select the Category"),

    'state' : fields.selection([
            ('vehicle_enter', 'Gate In'),
            ('vehicle_process', 'Gate Out'),
            ('vehicle_exit', 'Complete'),
            ],default='vehicle_enter'),
    'own_vehicle' : fields.boolean('Rented Vehicle', default=True),
    'transfer_order': fields.char('Transfer Order',size=32),
    'driver_text': fields.char('Driver',size=32),
	}


	def create(self, cr, uid, vals, context=None):
		sequence=self.pool.get('ir.sequence').get(cr, uid, 'inwardpass')
		seq_gin_shop = self.pool.get('ir.sequence').get(cr, uid, 'Genoutpass')
		vals['name']="In_"+vals['inward_Category']+"_"+sequence
		vals['gin'] = "Inward-"+vals['inward_Category']+"-"+seq_gin_shop
		return super(inwardpass, self).create(cr, uid, vals, context=context)
	_defaults = {
				'gin': lambda obj, cr, uid, context: '/',
				'out_gon': lambda obj, cr, uid, context: '/',

				'time_out': lambda obj, cr, uid, context: datetime.now(),
				'time_in': lambda obj, cr, uid, context: datetime.now(),
				'out_date': lambda obj, cr, uid, context: datetime.now(),
				'out_time_out': lambda obj, cr, uid, context: datetime.now(),
				'date': lambda obj, cr, uid, context: datetime.now(),
	 }		

class in_inward(osv.Model):
    _name = 'in_inward'
    _columns= {
    'uom': fields.char('UOM'),
    'qty': fields.char('QTY'),
    'item': fields.char('Item Category'),
    'in_inwardpass_id' : fields.many2one('inwardpass','Item Category'),
    }
#test

class out_inward(osv.Model):
    _name = 'out_inward'
    _columns= {
    'uom': fields.char('UOM'),
    'qty': fields.char('QTY'),
    'item': fields.char('Item Category'),
    'out_inwardpass_id' : fields.many2one('inwardpass','Item Category'),
    }


class in_inshop(osv.Model):
    _name = 'in_inshop'
    _columns= {
    'uom': fields.char('UOM'),
    'qty': fields.char('QTY'),
    'item': fields.char('Item Category'),
    'in_inwardshop_id' : fields.many2one('inwardshop','Item Category'),
    }

class out_inshop(osv.Model):
    _name = 'out_inshop'
    _columns= {
    'uom': fields.char('UOM'),
    'qty': fields.char('QTY'),
    'item': fields.char('Item Category'),
    'out_inwardshop_id' : fields.many2one('inwardshop','Item Category'),
    }    

  

class in_inret(osv.Model):
    _name = 'in_inret'
    _columns= {
    'item_des': fields.char('Item Description'),
    'brought_in_qty': fields.integer('Brought In QTY'),
    'qty_used': fields.char('QTY Used'),
    'diff': fields.integer('Difference (If any)', readonly=True),
    'brought_out_qty': fields.integer('Brought Out QTY'),
    'in_inwardret_id' : fields.many2one('inwardret','Item Category'),
    }
    def onchange_result(self, cr, uid, ids, brought_in_qty, brought_out_qty, context=None):
    	res = {}
    	if brought_in_qty and brought_out_qty:
    		res['diff'] = brought_in_qty - brought_out_qty
    	return {'value': res}


class out_inret(osv.Model):
    _name = 'out_inret'
    _columns= {
    'item_des': fields.char('Item Description'),
    'brought_in_qty': fields.integer('Brought In QTY'),
    'qty_used': fields.char('QTY Used'),
    'diff': fields.integer('Difference (If any)', readonly=True),
    'brought_out_qty': fields.integer('Brought Out QTY'),
    'out_inwardret_id' : fields.many2one('inwardret','Item Category'),
    }
    def onchange_result(self, cr, uid, ids, brought_in_qty, brought_out_qty, context=None):
    	res = {}
    	if brought_in_qty and brought_out_qty:
    		res['diff'] = brought_in_qty - brought_out_qty
    	return {'value': res}


class in_outret(osv.Model):
    _name = 'in_outret'
    _columns= {
    'item_des': fields.char('Item Description'),
    'brought_in_qty': fields.integer('Brought In QTY'),
    'qty_used': fields.char('QTY Used'),
    'diff': fields.integer('Difference (If any)', readonly=True),
    'brought_out_qty': fields.integer('Brought Out QTY'),
    'in_outwardret_id' : fields.many2one('out_inwardret','Item Category'),
    }
    def onchange_result(self, cr, uid, ids, brought_in_qty, brought_out_qty, context=None):
    	res = {}
    	if brought_in_qty and brought_out_qty:
    		res['diff'] = brought_in_qty - brought_out_qty
    	return {'value': res}


class out_outret(osv.Model):
    _name = 'out_outret'
    _columns= {
    'item_des': fields.char('Item Description'),
    'brought_in_qty': fields.integer('Brought In QTY'),
    'qty_used': fields.char('QTY Used'),
    'diff': fields.integer('Difference (If any)', readonly=True),
    'brought_out_qty': fields.integer('Brought Out QTY'),
    'out_outwardret_id' : fields.many2one('out_inwardret','Item Category'),
    }
    def onchange_result(self, cr, uid, ids, brought_in_qty, brought_out_qty, context=None):
    	res = {}
    	if brought_in_qty and brought_out_qty:
    		res['diff'] = brought_in_qty - brought_out_qty
    	return {'value': res}    	


class stock_warehouse(osv.Model):
	_inherit="stock.location"


#new api code for gate pass
from openerp import models, fields, api
class gate_pass_outwardpass_inherit(models.Model):
	_inherit = 'outwardpass'
	@api.one
	def vehicle_enter(self):
		self.write({'state': 'vehicle_enter'})

	@api.one
	def vehicle_process(self):
		self.write({'state': 'vehicle_process'})
		self.gin = self.select_sequence.prefix + str(self.select_sequence.number_next_actual)
		self.select_sequence.number_next_actual = self.select_sequence.number_next_actual + 1
	@api.one
	def vehicle_exit(self):
		self.write({'state': 'vehicle_exit'})
		datetime_in = self.time_in
		datetime_out = self.time_out
		dt_s_obj = datetime.strptime(datetime_in,"%Y-%m-%d %H:%M:%S")
		dt_e_obj = datetime.strptime(datetime_out,"%Y-%m-%d %H:%M:%S")
		timedelta = dt_s_obj - dt_e_obj
		print timedelta
		days_hours  = timedelta.days * 24
		sec = timedelta.seconds
		float_hours = sec/3600.0
		self.time_duration = days_hours + float_hours
		if self.trip_management_field:	
			self.trip_management_field.actual_trip_time = days_hours + float_hours
			self.trip_management_field.actual_trip_route_distance = self.gpi_odoo_meter - self.gp_odoo_meter

		self.odoometer_difference = self.gpi_odoo_meter - self.gp_odoo_meter	
		
	@api.onchange('fleet_vehicle_id')
	def on_change_vehicle(self):
		self.gp_odoo_meter = self.fleet_vehicle_id.odometer
		self.gpi_odoo_meter = self.fleet_vehicle_id.odometer
		self.vehicle_type_fleet = self.fleet_vehicle_id.vehicle_type_fleet
	
	@api.onchange('trip_management_field')
	def onchange_trip_field(self):
		self.fleet_vehicle_id = self.trip_management_field.vehicle
		self.gp_odoo_meter = self.trip_management_field.vehicle.odometer
		self.gpi_odoo_meter = self.trip_management_field.vehicle.odometer
		self.out_driver = self.trip_management_field.driver_id

	
	@api.onchange('outward_Category')
	def onchange_outward_Category_field(self):
		sequence = self.env['ir.sequence']
		if self.outward_Category:
			if self.outward_Category == 'Shop':
				search_seq = sequence.search([('name','=','outshopseq')])
				self.select_sequence = search_seq
			if self.outward_Category == 'Market_Purchase':
				search_seq_market = sequence.search([('name','=','outmarketseq')])
				self.select_sequence = search_seq_market
			if self.outward_Category == 'General':
				search_seq_gen = sequence.search([('name','=','outgeneralseq')])
				self.select_sequence = search_seq_gen
			if self.outward_Category == 'Returnable':
				search_seq_ret = sequence.search([('name','=','outreturnableseq')])
				self.select_sequence = search_seq_ret
# For Write method code
	@api.multi
	def write(self, values):
		result = super(gate_pass_outwardpass_inherit, self).write(values)
		fuel_logs_rec = self.env['fleet.vehicle.odometer'].search([('vehicle_id','=',self.fleet_vehicle_id.id)])
		#print fuel_logs_rec[-1]
		#print fuel_logs_rec[-1].value
		if self.gpi_odoo_meter:
			fuel_logs_rec[-1].value = self.gpi_odoo_meter
		return result

	@api.multi
	def odoometer_value_pass(self):
		check_odometer = self.gpi_odoo_meter
		check_vehicle_id = self.trip_management_field.vehicle.id
		check_vehicle_frm = self.fleet_vehicle_id.id
		if self.fleet_vehicle_id:
			self.fleet_vehicle_id.odometer = check_odometer

	@api.multi
	def odoometer_value_pass_gp(self):
		check_odometer = self.gp_odoo_meter
		check_vehicle_id = self.trip_management_field.vehicle.id
		check_vehicle_frm = self.fleet_vehicle_id.id
		if self.fleet_vehicle_id:
			self.fleet_vehicle_id.odometer = check_odometer
		fuel_logs_rec = self.env['fleet.vehicle.odometer'].search([])

class gate_pass_inwardpass_inherit(models.Model):
	_inherit = 'inwardpass'
	@api.one
	def vehicle_enter(self):
		self.write({'state': 'vehicle_enter'})
	@api.one
	def vehicle_process(self):
		self.write({'state': 'vehicle_process'})
		self.out_gon = self.select_sequence.prefix + str(self.select_sequence.number_next_actual)
		self.select_sequence.number_next_actual = self.select_sequence.number_next_actual + 1
	@api.one
	def vehicle_exit(self):
		self.write({'state': 'vehicle_exit'})
		datetime_in = self.time_in
		datetime_out = self.time_out
 		dt_s_obj = datetime.strptime(datetime_in,"%Y-%m-%d %H:%M:%S")
 		dt_e_obj = datetime.strptime(datetime_out,"%Y-%m-%d %H:%M:%S")
 		timedelta = dt_e_obj - dt_s_obj
 		days_hours  = timedelta.days * 24
 		sec = timedelta.seconds
 		float_hours = sec/3600.0
 		self.time_duration = days_hours + float_hours
 		if self.trip_management_field:	
			self.trip_management_field.actual_trip_time = days_hours + float_hours
			self.trip_management_field.actual_trip_route_distance = self.gpi_odoo_meter - self.gp_odoo_meter

		self.odoometer_difference = self.gpi_odoo_meter - self.gp_odoo_meter	
	@api.onchange('fleet_vehicle_id')
	def on_change_vehicle(self):
		self.gp_odoo_meter = self.fleet_vehicle_id.odometer
		self.gpi_odoo_meter = self.fleet_vehicle_id.odometer			
	@api.onchange('trip_management_field')
	def onchange_trip_field(self):
		self.fleet_vehicle_id = self.trip_management_field.vehicle
		self.gp_odoo_meter = self.trip_management_field.vehicle.odometer
		self.gpi_odoo_meter = self.trip_management_field.vehicle.odometer
		self.out_driver = self.trip_management_field.driver_id

	@api.onchange('inward_Category')
	def onchange_inward_Category_field(self):
		sequence = self.env['ir.sequence']
		if self.inward_Category:
			if self.inward_Category == 'supplier':
				search_seq = sequence.search([('name','=','insupseq')])
				self.select_sequence = search_seq
			if self.inward_Category == 'general':
				search_seq_gen = sequence.search([('name','=','ingeneralseq')])
				self.select_sequence = search_seq_gen
			if self.inward_Category == 'returnable':
				search_seq_ret = sequence.search([('name','=','inreturnableseq')])
				self.select_sequence = search_seq_ret

# For Write method code
	@api.multi
	def write(self, values):
		result = super(gate_pass_inwardpass_inherit, self).write(values)
		fuel_logs_rec = self.env['fleet.vehicle.odometer'].search([('vehicle_id','=',self.fleet_vehicle_id.id)])
		if self.gpi_odoo_meter:
			fuel_logs_rec[-1].value = self.gpi_odoo_meter
		return result

	@api.multi
	def odoometer_value_pass(self):
		check_odometer = self.gpi_odoo_meter
		check_vehicle_id = self.trip_management_field.vehicle.id
		check_vehicle_frm = self.fleet_vehicle_id.id
		if self.fleet_vehicle_id:
			self.fleet_vehicle_id.odometer = check_odometer


	@api.multi
	def odoometer_value_pass_gp(self):
		check_odometer = self.gp_odoo_meter
		check_vehicle_id = self.trip_management_field.vehicle.id
		check_vehicle_frm = self.fleet_vehicle_id.id
		if self.fleet_vehicle_id:
			self.fleet_vehicle_id.odometer = check_odometer
		fuel_logs_rec = self.env['fleet.vehicle.odometer'].search([])
		