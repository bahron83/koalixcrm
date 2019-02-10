# -*- coding: utf-8 -*-
from os import path
from wsgiref.util import FileWrapper
from django.contrib import messages
from subprocess import CalledProcessError
from django.views.generic import View
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from koalixcrm.crm.exceptions import *
#from koalixcrm.crm.contact.customer import Customer
#from koalixcrm.crm.contact.customer import *
import koalixcrm
from koalixcrm.crm import models
from django.template.response import TemplateResponse
from koalixcrm.crm.const.postaladdressprefix import *
#from django.views.decorators.cache import cache_page


'''class CustomerView(View):
    def get(self, request, *args, **kwargs):
        customer =  models.Customer.objects.all().first()
        out = customer.export(models.Customer.EXPORT_FIELDS_EXTENDED)
        
        return json_response(out)'''

def customer_resume(request, id, template='customer_resume.html'):
    try:
        customer = models.Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        raise Http404 

    main_address = customer.postal_addresses.filter(prefix='F').first()
    main_contact = customer.person_association.first()
    main_contact_prefix = None
    if main_contact:
        l = [p for p in POSTALADDRESSPREFIX if p[0] == main_contact.person.prefix]
        if l:
            main_contact_prefix = _(l[0][1])
    first_call = customer.calls.all().order_by('date_of_creation').first()
    last_call = customer.calls.all().order_by('-date_of_creation').first()
    context_dict = {
        'customer': customer,
        'main_address': main_address,
        'main_contact': main_contact,
        'main_contact_prefix': main_contact_prefix,
        'first_call': first_call,
        'last_call': last_call
    }
    return TemplateResponse(
        request, template, context=context_dict)

def export_pdf(calling_model_admin, request, document, redirect_to):
    """This method exports PDFs provided by different Models in the crm application

        Args:
          calling_model_admin (ModelAdmin):  The calling ModelAdmin must be provided for error message response.
          request: The request User is to know where to save the error message
          document (Contract):  The model from which a PDF should be exported
          redirect_to (str): String that describes to where the method should redirect in case of an error

        Returns:
          HTTpResponse with a PDF when successful
          HTTpResponseRedirect when not successful

        Raises:
          raises Http404 exception if anything goes wrong"""
    try:
        pdf = document.create_pdf()
        response = HttpResponse(FileWrapper(open(pdf, 'rb')), content_type='application/pdf')
        response['Content-Length'] = path.getsize(pdf)
    except (TemplateSetMissing, UserExtensionMissing, CalledProcessError, UserExtensionEmailAddressMissing, UserExtensionPhoneAddressMissing) as e:
        if isinstance(e, UserExtensionMissing):
            response = HttpResponseRedirect(redirect_to)
            calling_model_admin.message_user(request, _("User Extension Missing"))
        elif isinstance(e, UserExtensionEmailAddressMissing):
            response = HttpResponseRedirect(redirect_to)
            calling_model_admin.message_user(request, _("User Extension Email Missing"))
        elif isinstance(e, UserExtensionPhoneAddressMissing):
            response = HttpResponseRedirect(redirect_to)
            calling_model_admin.message_user(request, _("User Extension Phone Missing"))
        elif isinstance(e, TemplateSetMissing):
            response = HttpResponseRedirect(redirect_to)
            calling_model_admin.message_user(request, _("Templateset Missing"))
        elif isinstance(e, TemplateFOPConfigFileMissing):
            response = HttpResponseRedirect(redirect_to)
            calling_model_admin.message_user(request, _("Fop Config File Missing in TemplateSet"))
        elif isinstance(e, TemplateXSLTFileMissing):
            response = HttpResponseRedirect(redirect_to)
            calling_model_admin.message_user(request, _("XSLT File Missing in TemplateSet"))
        elif type(e) == CalledProcessError:
            response = HttpResponseRedirect(redirect_to)
            calling_model_admin.message_user(request, e.output)
        else:
            raise Http404
    return response


def create_new_document(calling_model_admin, request, calling_model, requested_document_type, redirect_to):
    """This method exports PDFs provided by different Models in the crm application

        Args:
          calling_model_admin (ModelAdmin):  The calling ModelAdmin must be provided for error message response.
          request: The request User is to know where to save the error message
          calling_model (Contract or SalesDocument):  The model from which a new document shall be created
          requested_document_type (str): The document type name that shall be created
          redirect_to (str): String that describes to where the method should redirect in case of an error

        Returns:
          HTTpResponse with a PDF when successful
          HTTpResponseRedirect when not successful

        Raises:
          raises Http404 exception if anything goes wrong"""
    try:
        new_document = requested_document_type()
        new_document.create_from_reference(calling_model)
        calling_model_admin.message_user(request, _(str(new_document) +
                                                    " created"))
        response = HttpResponseRedirect('/admin/crm/'+
                                        new_document.__class__.__name__.lower()+
                                        '/'+
                                        str(new_document.id))
    except (TemplateSetMissingInContract, TemplateMissingInTemplateSet) as e:
        if isinstance(calling_model, koalixcrm.crm.documents.contract.Contract):
            contract = calling_model
        else:
            contract = calling_model.contract
        if isinstance(e, TemplateSetMissingInContract):
            response = HttpResponseRedirect('/admin/crm/contract/'+
                                            str(contract.id))
            calling_model_admin.message_user(request, _("Missing Templateset "),
                                             level=messages.ERROR)
        elif isinstance(e, TemplateMissingInTemplateSet):
            response = HttpResponseRedirect('/admin/djangoUserExtension/templateset/' +
                                            str(contract.default_template_set.id))
            calling_model_admin.message_user(request,
                                             (_("Missing template for ")+
                                              new_document.__class__.__name__),
                                             level=messages.ERROR)
        else:
            raise Http404
    return response

CACHE_TTL = 120

#customer_view = cache_page(CACHE_TTL)(CustomerView.as_view())
#customer_view = CustomerView.as_view()
