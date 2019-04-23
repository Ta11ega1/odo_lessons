# -*- coding: utf-8 -*-
import xlsxwriter
import base64, cStringIO
import xlwt
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.tools.translate import _
import os, sys, stat

from openerp.http import request
from openerp import http
from openerp.addons.web.controllers.main import serialize_exception,content_disposition


class Binary(http.Controller):
    @http.route('/web/binary/download_report', type='http', auth="public")
    @serialize_exception
    def download_xls_document(self, path, filename, **kw):
        with open(path, "rb") as pdf_file:
            return request.make_response(pdf_file.read(),
                                     [('Content-Type', 'application/octet-stream'),
                                      ('Content-Disposition', content_disposition(filename))])
									  
class detalles(models.TransientModel):
 	_name = 'mi_modulo.mi_tabla_'
	
	file = fields.Binary()
	filename = fields.Char()
	
	@api.multi
	def imprimir_excel(self, context=None):
		data2 = cStringIO.StringIO()
		#workbook = xlsxwriter.Workbook(data2, {'in_memory': True})
		workbook = xlsxwriter.Workbook('nuevohello.xlsx')
		worksheet = workbook.add_worksheet()
		if context is None:
			context = {}
		active_ids = context.get('active_ids', []) or []
		registros = self.env['mi_modulo.mi_tabla'].browse(active_ids)
		
		worksheet.write('A1', 'Nombre')
		worksheet.write('B1', 'Descripcion')
		worksheet.write('C1', 'Seleccion')
		contador = 2
		
		for linea in registros:
			worksheet.write('A'+str(contador), linea.name)
			worksheet.write('B'+str(contador), linea.description)
			worksheet.write('C'+str(contador), linea.selection)
			contador += 1

		

		workbook.close()
		return {
			'type': 'ir.actions.act_url',
			'url': '/web/binary/download_report?path=%s&filename=%s' % ('C:/Program Files (x86)/Odoo 10.0/nuevohello.xlsx', 'nuevohello.xlsx'),
			'target': 'blank',
		}
	
	@api.multi
	def invoice_confirm_dte(self):
		path = os.chmod('C:\Users\Systcom\Downloads', 0666)
		
		"""return {
			'view_type': 'form',
			'view_mode': 'form',
			'res_model': 'mi_modulo.mi_tabla_',
			'type': 'ir.actions.act_window',
			'target': 'new',
			'context': {'default_file':self.file, 'default_filename':self.filename},
		}"""
		

	def eliminar_excel(self):
		os.remove('nuevohello.xlsx')
	