from openerp.osv import osv,fields
from datetime import date, datetime
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
	'supplier_details': fields.many2one('res.partner','Supplier Details'),
	'inward_id' : fields.one2many('inward','inwardpass_id',string='Details'),
	'remarks' : fields.text('Remarks'),
	'gi_seal': fields.char('Seal In'),
	'go_seal': fields.char('Seal Out'),
	'vehicle_num' : fields.char('Vehicle Number',size=32),
	'fleet_vehicle_id' : fields.many2one('fleet.vehicle','Vehicle'),

	'out_date' : fields.date('Date', ),
	'out_nature' : fields.boolean('Return or Rejection'),
	'out_gon' : fields.char('GON #',),
	'out_sron' : fields.char('SRON Ref.',size=32),
	'out_time_out' : fields.datetime('Time Out',),
	'out_vehicle' : fields.char('Vehicle',size=32),
	'out_supplier_details': fields.many2one('res.partner','Supplier Details'),
	'out_remarks' : fields.text('Remarks'),
	'trip_management_field': fields.many2one('trip.management','Trip'),
	'gp_odoo_meter': fields.float("Odoo Meter Exit"),
	'gpi_odoo_meter': fields.float("Odoo Meter Enterance"),
	'lc_pc' : fields.selection([
            ('lc', 'LC'),
            ('pc', 'PC'),
            ],default='', string="LC or PO"),
    'state' : fields.selection([
            ('vehicle_enter', 'Gate In'),
            ('vehicle_process', 'Gate Out'),
            ('vehicle_exit', 'Validate'),
            ],default='vehicle_enter')
	}


	def create(self, cr, uid, vals, context=None):
		sequence=self.pool.get('ir.sequence').get(cr, uid, 'inwardpass')
		vals['name']=sequence
		vals['gin'] = sequence
		vals['out_gon'] = sequence
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

class inward(osv.Model):
    _name = 'inward'
    _columns= {
    'uom': fields.char('UOM'),
    'qty': fields.char('QTY'),
    'item': fields.char('Item Category'),
    'inwardpass_id' : fields.many2one('inwardpass','Item Category'),
    }
#test






class inwardshop(osv.Model):
	_name='inwardshop'
	_inherit = ['mail.thread', 'ir.needaction_mixin']
	_columns= {
	'name': fields.char('Name',readonly=True),
	'date' : fields.date('Date', ),
	'gin' : fields.char('GIN #',size=32 ),
	'srin' : fields.char('SRIN #',size=32),
	'branch' : fields.many2one('stock.location','Branch Name'),
	'time_in' : fields.datetime('Time In', ),
	'vehicle_type' : fields.char('Vehicle Type',size=32),
	'inshop_id' : fields.one2many('inshop','inwardshop_id',string='Details'),
	'fleet_vehicle_id' : fields.many2one('fleet.vehicle','Vehicle'),
	'driver' : fields.many2one('res.partner','Driver',domain="['|',('customer','=',True),('employee','=',True)]"),
	'remarks' : fields.text('Remarks'),

	'out_date' : fields.date('Date',),
	'out_gon' : fields.char('GON #',size=32 ),
	'out_sin' : fields.char('SIN #',size=32 ),
	'out_time_out' : fields.datetime('Time Out', ),
	'out_driver' : fields.many2one('res.partner','Driver',domain="['|',('customer','=',True),('employee','=',True)]"),
	'out_vehicle_type' : fields.char('Vehicle Type',size=32),
	'out_fleet_vehicle_id' : fields.many2one('fleet.vehicle','Vehicle'),
	#'out_show_reference': fields.boolean('Want to put reference ?'),
	'out_reference_field': fields.char('Reference', size=64),
	'out_remarks' : fields.text('Remarks'),
	'gi_seal' : fields.char('Seal In'),
	'go_seal' : fields.char('Seal Out'),
	'trip_management_field': fields.many2one('trip.management','Trip'),
	'gp_odoo_meter': fields.float("Odoo Meter Exit"),
	'gpi_odoo_meter': fields.float("Odoo Meter Enterance"),
    'state' : fields.selection([
            ('vehicle_enter', 'Gate Out'),
            ('vehicle_process', 'Gate In'),
            ('vehicle_exit', 'Validate'),
            ],default='vehicle_enter')
	}
#	def on_change_vehicle(self, cr, uid, ids, out_fleet_vehicle_id, context=None):
#		if not out_fleet_vehicle_id:
#			return {}
#		vehicle = self.pool.get('fleet.vehicle').browse(cr, uid, out_fleet_vehicle_id, context=context)
#		drive = vehicle.driver_id.id
#		print drive
#		return {
#					'value': {
#					'driver': drive,
#				}
#				}


	def create(self, cr, uid, vals, context=None):
		sequence=self.pool.get('ir.sequence').get(cr, uid, 'inwardshop')
		vals['name']=sequence
		vals['gin'] = sequence
		vals['out_gon'] = sequence
		return super(inwardshop, self).create(cr, uid, vals, context=context)
	_defaults = {
				'gin': lambda obj, cr, uid, context: '/',
				'out_gon': lambda obj, cr, uid, context: '/',

				#'time_out': lambda obj, cr, uid, context: datetime.now(),
				'time_in': lambda obj, cr, uid, context: datetime.now(),
				'out_date': lambda obj, cr, uid, context: datetime.now(),
				'out_time_out': lambda obj, cr, uid, context: datetime.now(),
				'date': lambda obj, cr, uid, context: datetime.now(),
				 }


class inshop(osv.Model):
    _name = 'inshop'
    _columns= {
    'uom': fields.char('UOM'),
    'qty': fields.char('QTY'),
    'item': fields.char('Item Category'),
    'inwardshop_id' : fields.many2one('inwardshop','Item Category'),
    }






class inwardgen(osv.Model):
	_name='inwardgen'
	_inherit = ['mail.thread', 'ir.needaction_mixin']
	_columns= {
	'name': fields.char('Name',readonly=True),
	'date' : fields.date('Date', ),
	'gin' : fields.char('GIN #',size=32 ),
	'document_ref' : fields.char('Document Ref #',size=32),
	'vehicle' : fields.char('Vehicle',size=32),
	'time_in' : fields.datetime('Time In', ),
	'vehicle_type' : fields.char('Vehicle Type',size=32),
	'ingen_id' : fields.one2many('ingen','inwardgen_id',string='Details'),
	'remarks' : fields.text('Remarks'),
	'fleet_vehicle_id' : fields.many2one('fleet.vehicle','Vehicle'),

	'out_date' : fields.date('Date',),
	'out_gon' : fields.char('GON #',size=32 ),
	'out_document_ref' : fields.char('Document Ref #',size=32),
	'out_time_out' : fields.datetime('Time Out', ),
	'out_vehicle' : fields.char('Vehicle',size=32),
	'out_vehicle_type' : fields.char('Vehicle Type',size=32),
	'out_remarks' : fields.text('Remarks'),
	'gi_seal' : fields.char('Seal In'),
	'go_seal' : fields.char('Seal Out'),
	'trip_management_field': fields.many2one('trip.management','Trip'),
	'gp_odoo_meter': fields.float("Odoo Meter Exit"),
	'gpi_odoo_meter': fields.float("Odoo Meter Enterance"),

    'state' : fields.selection([
            ('vehicle_enter', 'Gate Out'),
            ('vehicle_process', 'Gate In'),
            ('vehicle_exit', 'Validate'),
            ],default='vehicle_enter')
	}

	def create(self, cr, uid, vals, context=None):
		sequence=self.pool.get('ir.sequence').get(cr, uid, 'inwardgen')
		vals['name']=sequence
		vals['gin'] = sequence
		vals['out_gon'] = sequence
		return super(inwardgen, self).create(cr, uid, vals, context=context)
	_defaults = {
				'gin': lambda obj, cr, uid, context: '/',
				'out_gon': lambda obj, cr, uid, context: '/',

				#'time_out': lambda obj, cr, uid, context: datetime.now(),
				'time_in': lambda obj, cr, uid, context: datetime.now(),
				'out_date': lambda obj, cr, uid, context: datetime.now(),
				'out_time_out': lambda obj, cr, uid, context: datetime.now(),
				'date': lambda obj, cr, uid, context: datetime.now(),
				 }

class ingen(osv.Model):
    _name = 'ingen'
    _columns= {
    'uom': fields.char('UOM'),
    'qty': fields.char('QTY'),
    'item': fields.char('Item Category'),
    'inwardgen_id' : fields.many2one('inwardgen','Item Category'),
    }


class inwardret(osv.Model):
	_name='inwardret'
	_inherit = ['mail.thread', 'ir.needaction_mixin']
	_columns= {
	'name': fields.char('Name',readonly=True),
	'dept': fields.char('Department/Section', size=32),
	'date_out' : fields.date('Date Out', ),
	'date_in' : fields.date('Date In', ),
	'gin' : fields.char('GIN #',size=32 ),
	'document_ref' : fields.char('Document Ref #',size=32),
	'time_out' : fields.datetime('Time Out',),
	'vehicle' : fields.char('Vehicle',size=32),
	'time_in' : fields.datetime('Time In',),
	'workers': fields.char('No of Workers',size=32),
	'vehicle_type' : fields.char('Vehicle Type',size=32),
	'inret_id' : fields.one2many('inret','inwardret_id',string='Details'),
	'stock_location_id' : fields.many2one('stock.location','Dept'),
	'remarks' : fields.text('Remarks'),
	'fleet_vehicle_id' : fields.many2one('fleet.vehicle','Vehicle'),

	'out_dept': fields.char('Department/Section', size=32),
	'out_date_out' : fields.date('Date Out', ),
	'out_date_in' : fields.date('Date In', ),
	'out_gon' : fields.char('GON #',size=32 ),
	'out_document_ref' : fields.char('Document Ref #',size=32),
	'out_time_out' : fields.datetime('Time Out',),
	'out_vehicle' : fields.char('Vehicle',size=32),
	'out_time_in' : fields.datetime('Time In',),
	'out_vehicle_type' : fields.char('Vehicle Type',size=32),
	'out_stock_location_id' : fields.many2one('stock.location','Dept'),
	'out_remarks' : fields.text('Remarks'),
	'gi_seal' : fields.char('Seal In'),
	'go_seal' : fields.char('Seal Out'),
	'trip_management_field': fields.many2one('trip.management','Trip'),
	'gp_odoo_meter': fields.float("Odoo Meter Exit"),
	'gpi_odoo_meter': fields.float("Odoo Meter Enterance"),

    'state' : fields.selection([
            ('vehicle_enter', 'Gate Out'),
            ('vehicle_process', 'Gate In'),
            ('vehicle_exit', 'Validate'),
            ],default='vehicle_enter')
	}

	def create(self, cr, uid, vals, context=None):
		sequence=self.pool.get('ir.sequence').get(cr, uid, 'inwardret')
		vals['name']=sequence
		vals['gin'] = sequence
		vals['out_gon'] = sequence
		return super(inwardret, self).create(cr, uid, vals, context=context)
	_defaults = {
	'gin': lambda obj, cr, uid, context: '/',
	'out_gon': lambda obj, cr, uid, context: '/',
	'time_out': lambda obj, cr, uid, context: datetime.now(),
	'time_in': lambda obj, cr, uid, context: datetime.now(),
	'date_out': lambda obj, cr, uid, context: datetime.now(),
	'date_in': lambda obj, cr, uid, context: datetime.now(),
	'out_date_in': lambda obj, cr, uid, context: datetime.now(),
	'out_date_out': lambda obj, cr, uid, context: datetime.now(),
	'out_time_out': lambda obj, cr, uid, context: datetime.now(),
	'out_time_in': lambda obj, cr, uid, context: datetime.now(),
	 }

class inret(osv.Model):
    _name = 'inret'
    _columns= {
    'item_des': fields.char('Item Description'),
    'brought_in_qty': fields.integer('Brought In QTY'),
    'qty_used': fields.char('QTY Used'),
    'diff': fields.integer('Differenc (If any)', readonly=True),
    'brought_out_qty': fields.integer('Brought Out QTY'),
    'inwardret_id' : fields.many2one('inwardret','Item Category'),
    }
    def onchange_result(self, cr, uid, ids, brought_in_qty, brought_out_qty, context=None):
    	res = {}
    	if brought_in_qty and brought_out_qty:
    		res['diff'] = brought_in_qty - brought_out_qty
    	return {'value': res}

    


class fleet_vehicle(osv.Model):
	_inherit="fleet.vehicle"
	_columns= {
     'veh_reg': fields.one2many('inwardshop', 'fleet_vehicle_id', 'Vehicle'),
     }

class stock_warehouse(osv.Model):
	_inherit="stock.location"


#new api code for gate pass
from openerp import models, fields, api
class gate_pass_inwardpass_inherit(models.Model):
	_inherit = 'inwardpass'
	@api.one
	def vehicle_enter(self):
		self.write({'state': 'vehicle_enter'})
	@api.one
	def vehicle_process(self):
		self.write({'state': 'vehicle_process'})
	@api.one
	def vehicle_exit(self):
		self.write({'state': 'vehicle_exit'})
		if self.trip_management_field:
			datetime_in = self.time_in
			datetime_out = self.time_out
 			dt_s_obj = datetime.strptime(datetime_in,"%Y-%m-%d %H:%M:%S")
 			dt_e_obj = datetime.strptime(datetime_out,"%Y-%m-%d %H:%M:%S")
 			timedelta = dt_e_obj - dt_s_obj
 			sec = timedelta.seconds
 			float_hours = sec/3600.0
			self.trip_management_field.actual_trip_time = float_hours
	@api.onchange('fleet_vehicle_id')
	def on_change_vehicle(self):
		self.gp_odoo_meter = self.fleet_vehicle_id.odometer
		self.gpi_odoo_meter = self.fleet_vehicle_id.odometer			
	@api.onchange('trip_management_field')
	def onchange_trip_field(self):
		self.fleet_vehicle_id = self.trip_management_field.vehicle
		self.gp_odoo_meter = self.trip_management_field.vehicle.odometer
		self.gpi_odoo_meter = self.trip_management_field.vehicle.odometer


# For Write method code
	@api.multi
	def write(self, values):
		result = super(gate_pass_inwardpass_inherit, self).write(values)
		fuel_logs_rec = self.env['fleet.vehicle.odometer'].search([('vehicle_id','=',self.fleet_vehicle_id.id)])
		print fuel_logs_rec[-1]
		print fuel_logs_rec[-1].value
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
		print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
		print fuel_logs_rec
class gate_pass_inwardshop_inherit(models.Model):
	_inherit = 'inwardshop'
	@api.one
	def vehicle_enter(self):
		self.write({'state': 'vehicle_enter'})
	@api.one
	def vehicle_process(self):
		self.write({'state': 'vehicle_process'})
	@api.one
	def vehicle_exit(self):
		self.write({'state': 'vehicle_exit'})
		if self.trip_management_field:
			datetime_in = self.time_in
			datetime_out = self.time_out
 			dt_s_obj = datetime.strptime(datetime_in,"%Y-%m-%d %H:%M:%S")
 			dt_e_obj = datetime.strptime(datetime_out,"%Y-%m-%d %H:%M:%S")
 			timedelta = dt_e_obj - dt_s_obj
 			sec = timedelta.seconds
 			float_hours = sec/3600.0
			self.trip_management_field.actual_trip_time = float_hours
	@api.onchange('fleet_vehicle_id')
	def on_change_vehicle(self):
		self.gp_odoo_meter = self.fleet_vehicle_id.odometer
		self.gpi_odoo_meter = self.fleet_vehicle_id.odometer
		if self.fleet_vehicle_id:
			self.out_driver = self.fleet_vehicle_id.driver_id

	@api.onchange('trip_management_field')
	def onchange_trip_field(self):
		self.fleet_vehicle_id = self.trip_management_field.vehicle
		self.gp_odoo_meter = self.trip_management_field.vehicle.odometer
		self.gpi_odoo_meter = self.trip_management_field.vehicle.odometer
# Write Method
	@api.multi
	def write(self, values):
		result = super(gate_pass_inwardshop_inherit, self).write(values)
		fuel_logs_rec = self.env['fleet.vehicle.odometer'].search([('vehicle_id','=',self.fleet_vehicle_id.id)])
		print fuel_logs_rec[-1]
		print fuel_logs_rec[-1].value
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


class gate_pass_inwardgen_inherit(models.Model):
	_inherit = 'inwardgen'
	@api.one
	def vehicle_enter(self):
		self.write({'state': 'vehicle_enter'})
	@api.one
	def vehicle_process(self):
		self.write({'state': 'vehicle_process'})
	@api.one
	def vehicle_exit(self):
		self.write({'state': 'vehicle_exit'})
		if self.trip_management_field:
			datetime_in = self.time_in
			datetime_out = self.time_out
 			dt_s_obj = datetime.strptime(datetime_in,"%Y-%m-%d %H:%M:%S")
 			dt_e_obj = datetime.strptime(datetime_out,"%Y-%m-%d %H:%M:%S")
 			timedelta = dt_e_obj - dt_s_obj
 			sec = timedelta.seconds
 			float_hours = sec/3600.0
			self.trip_management_field.actual_trip_time = float_hours
	@api.onchange('fleet_vehicle_id')
	def on_change_vehicle(self):
		self.gp_odoo_meter = self.fleet_vehicle_id.odometer
		self.gpi_odoo_meter = self.fleet_vehicle_id.odometer			
	@api.onchange('trip_management_field')
	def onchange_trip_field(self):
		self.fleet_vehicle_id = self.trip_management_field.vehicle
		self.gp_odoo_meter = self.trip_management_field.vehicle.odometer
		self.gpi_odoo_meter = self.trip_management_field.vehicle.odometer
#Write Method
	@api.multi
	def write(self, values):
		result = super(gate_pass_inwardgen_inherit, self).write(values)
		fuel_logs_rec = self.env['fleet.vehicle.odometer'].search([('vehicle_id','=',self.fleet_vehicle_id.id)])
		print fuel_logs_rec[-1]
		print fuel_logs_rec[-1].value
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

class gate_pass_inwardret_inherit(models.Model):
	_inherit = 'inwardret'
	@api.one
	def vehicle_enter(self):
		self.write({'state': 'vehicle_enter'})
	@api.one
	def vehicle_process(self):
		self.write({'state': 'vehicle_process'})
	@api.one
	def vehicle_exit(self):
		self.write({'state': 'vehicle_exit'})
		if self.trip_management_field:
			datetime_in = self.time_in
			datetime_out = self.time_out
 			dt_s_obj = datetime.strptime(datetime_in,"%Y-%m-%d %H:%M:%S")
 			dt_e_obj = datetime.strptime(datetime_out,"%Y-%m-%d %H:%M:%S")
 			timedelta = dt_e_obj - dt_s_obj
 			sec = timedelta.seconds
 			float_hours = sec/3600.0
			self.trip_management_field.actual_trip_time = float_hours
	@api.onchange('fleet_vehicle_id')
	def on_change_vehicle(self):
		self.gp_odoo_meter = self.fleet_vehicle_id.odometer
		self.gpi_odoo_meter = self.fleet_vehicle_id.odometer			
	@api.onchange('trip_management_field')
	def onchange_trip_field(self):
		self.fleet_vehicle_id = self.trip_management_field.vehicle
		self.gp_odoo_meter = self.trip_management_field.vehicle.odometer
		self.gpi_odoo_meter = self.trip_management_field.vehicle.odometer
#Write Method
	@api.multi
	def write(self, values):
		result = super(gate_pass_inwardret_inherit, self).write(values)
		fuel_logs_rec = self.env['fleet.vehicle.odometer'].search([('vehicle_id','=',self.fleet_vehicle_id.id)])
		print fuel_logs_rec[-1]
		print fuel_logs_rec[-1].value
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