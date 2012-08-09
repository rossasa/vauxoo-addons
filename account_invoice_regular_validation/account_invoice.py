# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2010 Vauxoo - http://www.vauxoo.com/
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
############################################################################
#    Coded by: Luis Torres (luis_t@vauxoo.com)
############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from osv import fields, osv
from tools.translate import _

class account_invoice(osv.osv):
    _inherit='account.invoice'
    
    def action_move_create(self, cr, uid, ids, context=None):
        if not context:
            context={}
        for lin in self.browse(cr,uid,ids):
            for lins in lin.invoice_line:
                if lins.account_id.type<>'other':
                    raise osv.except_osv(_('Error!'),_("Can not be used different types of accounts to 'other' in the lines of the invoice!"))
        res = super(account_invoice,self).action_move_create(cr, uid, ids, context=context)
        return res
account_invoice()

class account_invoice_line(osv.osv):
    _inherit='account.invoice.line'
    
    _columns={
        'account_id': fields.many2one('account.account', 'Account', required=True, readonly=True, domain=[('type','=','other')], states={'draft':[('readonly',False)]}, help="The partner account used for this invoice."),
    }
account_invoice_line()
