# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2019-TODAY OPeru.
#    Author      :  Grupo Odoo S.A.C. (<http://www.operu.pe>)
#
#    This program is copyright property of the author mentioned above.
#    You can`t redistribute it and/or modify it.
#
###############################################################################

from odoo import api, fields, models

class ProductTemplate(models.Model):
        _name = 'product.template'
        _inherit = 'product.template'

        l10n_pe_edi_product_code = fields.Many2one("l10n_pe_edi.catalog.25", string='Product code SUNAT')
