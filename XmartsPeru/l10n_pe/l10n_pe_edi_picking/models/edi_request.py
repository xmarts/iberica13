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

from odoo import models, fields, api, _
from datetime import datetime, date, timedelta
import json, requests
import urllib3
from odoo.exceptions import UserError

class EdiRequest(models.Model):
    _inherit = 'l10n_pe_edi.request'

    type = fields.Selection(selection_add=[('picking', 'Picking')])
    