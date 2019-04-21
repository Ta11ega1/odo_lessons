# -*- coding: utf-8 -*-
import xlsxwriter
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.tools.translate import _
import base64, cStringIO

class detalles(models.TransientModel):
 	_name = 'mi_modulo.mi_tabla_'
	
	
	@api.multi
	def invoice_confirm_dte(self, context=None):
		output = cStringIO.StringIO()
		self.env.cr.execute('select name, description, selection from mi_modulo_mi_tabla')
		datos = self.env.cr.fetchall()
		workbook = xlsxwriter.Workbook(output, {'in_memory': True})
		#workbook = xlsxwriter.Workbook('hola.xlsx')
		worksheet = workbook.add_worksheet()
		if context is None:
			context = {}
		active_ids = context.get('active_ids', []) or []
		registros = self.env['mi_modulo.mi_tabla'].browse(active_ids)
		#cells = xlsxwriter.utility.xl_range(0,0, 1, 1)
		#worksheet.add_table(cells, {'data': 'hola', 'total_row', 1, 'columns': 1})
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
		output.seek(0)
		vals = {
			'name': 'something',
			'datas_fname': 'name.xlsx',
			'description': 'XXXXXXXXXXXXX',
			'parent_id': 'mi_modulo_4',
			'type': 'binary',
			'db_datas': base64.encodestring(output.read()),
        }        
        file_id = self.pool.get('ir.attachment').create(vals,context=context)
		"""return {
			'view_type': 'form',
			'view_mode': 'form',
			'res_model': 'mi_modulo.mi_tabla_',
			'type': 'ir.actions.act_window',
			'target': 'new',
			'context': {'default_file':base64.encodestring(output.read()), 'default_filename':'hola.xlsx'}
		
		}"""
		
		
       