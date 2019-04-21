# -*- coding: utf-8 -*-
from openerp import models, fields
from odoo.tools.translate import _

class mi_modulo_mi_tabla(models.Model):
    _name = "mi_modulo.mi_tabla"
     
    name = fields.Char('Nombre', size=25)
    description = fields.Char('Descripción', size=255)

    selection = fields.Selection([
    	('insignificante', ('Insignificante')),
    	('menor', ('Menor')),
    	('moderado', ('Moderado')),
    	('peligroso', ('Peligroso')),
    	('catastrófico', ('Catastrófico'))], 
    	string="Selecciona")

    #selection = fields.Selection(Selection[('hola','mundo','hellow','world','end')])

   # @api.multi
   # def imprimir_datalles(self):
        
	
	
		