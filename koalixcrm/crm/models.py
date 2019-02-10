# -*- coding: utf-8 -*-
from django.core import files
import datetime

class Exportable(object):
    """
    Simple interface to export classes as serializable dicts
    """
    EXPORT_FIELDS = []

    def export(self, fieldset=None):
        """
        """
        out = {}
        if fieldset is None:
            fieldset = self.EXPORT_FIELDS
        for fname, fsource in fieldset:
            val = getattr(self, fsource, None)
            if callable(val):
                val = val()
            elif isinstance(val, files.File):
                try:
                    val = val.url
                except ValueError:
                    val = None
            elif isinstance(val, (datetime.date, datetime.datetime)):
                val = val.isoformat()
            out[fname] = val
        return out

from koalixcrm.crm.contact.contact import *
from koalixcrm.crm.contact.customergroup import *
from koalixcrm.crm.contact.customer import *
from koalixcrm.crm.contact.postaladdress import *
from koalixcrm.crm.contact.customerbillingcycle import *
from koalixcrm.crm.contact.emailaddress import *
from koalixcrm.crm.contact.phoneaddress import *
from koalixcrm.crm.contact.supplier import *

from koalixcrm.crm.documents.contract import Contract, PostalAddressForContract
from koalixcrm.crm.documents.contract import PhoneAddressForContract, EmailAddressForContract
from koalixcrm.crm.documents.salesdocumentposition import Position, SalesDocumentPosition
from koalixcrm.crm.documents.salesdocument import SalesDocument, PostalAddressForSalesDocument
from koalixcrm.crm.documents.salesdocument import EmailAddressForSalesDocument, PhoneAddressForSalesDocument
from koalixcrm.crm.documents.salesdocument import TextParagraphInSalesDocument
from koalixcrm.crm.documents.invoice import Invoice
from koalixcrm.crm.documents.purchaseconfirmation import PurchaseConfirmation
from koalixcrm.crm.documents.purchaseorder import PurchaseOrder
from koalixcrm.crm.documents.quote import Quote

from koalixcrm.crm.product.currency import *
from koalixcrm.crm.product.price import *
from koalixcrm.crm.product.product import *
from koalixcrm.crm.product.tax import *
from koalixcrm.crm.product.unit import *
