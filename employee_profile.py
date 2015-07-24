from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
from openerp.tools import float_compare
import openerp.addons.decimal_precision as dp
import math
from math import modf

class ToolktHumanResources(models.Model):
	_inherit = "hr.employee"

	# Additional Fields for the employee profiles
	employee_number = fields.Char(string='Employee Number')
	employee_status = fields.Selection([('regular','Regular'), ('probationary','Probationary'), ('contractual','Contractual'), ('inter/ojt','Inter/OJT')], 'Employee Status', default='regular')
	taxpayer_identification_number = fields.Char(string='TIN')
	social_security_system_number = fields.Char(string='SSS Number')
	philippine_health_insurance_corporation_number = fields.Char(string='PHIC Number')
	home_development_mutual_fund = fields.Char(String='HDMF Number')
	date_hired = fields.Date(string='Date Hired')
	date_resigned = fields.Date(string='Date Resigned')
	