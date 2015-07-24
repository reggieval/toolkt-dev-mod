# -*- coding: utf-8 -*-
from openerp import models, fields, api, tools, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
import time
import datetime



class visitor1(models.Model):
	_name = 'visitor1'
	_description = 'Visitor table 1'


	STATUS_SELECTION = [
		('draft', 'New'),
		('submitted', 'Human Resources'),
		('admin', 'Administrator'),
		('done', 'Done'),
	]

	def draft_status(self, cr, uid, ids, context=None):
		return self.write(cr, uid, ids, {'status': 'draft'}, context=context)

	def submit_head(self, cr, uid, ids, context=None):
		return self.write(cr, uid, ids, {'status': 'head'}, context=context)

	def submit_custodian(self, cr, uid, ids, context=None):
		return self.write(cr, uid, ids, {'status': 'custodian'}, context=context)

	def submit_purchasing(self, cr, uid, ids, context=None):
		return self.write(cr, uid, ids, {'status': 'purchasing'}, context=context)

	status = fields.Selection(STATUS_SELECTION, string='Status', readonly=True, track_visibility='onchange', help='Info', select=True)

	name = fields.Many2one('hr.employee', string="Name", required=True)
	department = fields.Selection([('technical consultant', 'Technical Consultant'),('accounting','Accounting')])
	employee_number = fields.Char(related="name.employee_number", store=True, string="ID")



	visit = fields.One2many("visitor2", "table_id", "Visit")


class visitor2(models.Model):
	_name = 'visitor2'
	_description = 'Visitor table 2'

	visit_date = fields.Date("Visit Date")
	time_in = fields.Float("Time In")
	time_out = fields.Float("Time Out")
	client_company = fields.Many2one('res.partner', 'Client Name', )
	client_contact = fields.Char(related="client_company.phone", store=True, string='Client Contact')
	purpose = fields.Char("Purpose")

	table_id = fields.Many2one("visitor1", "Table")
