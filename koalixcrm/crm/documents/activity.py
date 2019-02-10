# -*- coding: utf-8 -*-

from datetime import *
from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext as _
from koalixcrm.crm.const.status import *
from koalixcrm.crm.models import Exportable

from koalixcrm.plugin import *

from django.utils import timezone

class Call(Exportable, models.Model):
    EXPORT_FIELDS = (
        ('staff', 'p_staff'),
        ('description', 'description'),
        ('date_of_creation', 'date_of_creation'),
        ('date_due', 'date_due'),
        ('last_modification', 'last_modification'),
        ('last_modified_by', 'p_last_modified_by'),
        ('status', 'p_status'),
    )

    staff = models.ForeignKey('auth.User', limit_choices_to={'is_staff': True}, blank=True, verbose_name=_("Staff"),
                              related_name="db_relcallstaff", null=True)
    description = models.TextField(verbose_name=_("Description"))
    date_of_creation = models.DateTimeField(verbose_name=_("Created at"), auto_now_add=True)
    date_due = models.DateTimeField(verbose_name=_("Date due"), default=datetime.now, blank=True)
    last_modification = models.DateTimeField(verbose_name=_("Last modified"), auto_now=True)
    last_modified_by = models.ForeignKey('auth.User', limit_choices_to={'is_staff': True}, blank=True, null=True,
                                         verbose_name=_("Last modified by"), related_name="db_calllstmodified")
    status = models.CharField(verbose_name=_("Status"), max_length=1, choices=CALLSTATUS, default="P")
    
    @property
    def p_staff(self):
        return self.staff.username

    @property
    def p_last_modified_by(self):
        return self.last_modified_by.username

    @property
    def p_status(self):
        l = [s for s in CALLSTATUS if s[0] == self.status]
        if l:
            return _(l[0][1])
    
    def __str__(self):
        return _("Call") + " " + str(self.id)

class CallOverdueFilter(admin.SimpleListFilter):
    title = _('Is call overdue')
    parameter_name = 'date_due'

    def lookups(self, request, model_admin):
        return (
            ('overdue', _('Overdue')),
            ('planned', _('Planned')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'planned':
            return queryset.filter(date_due__gt=timezone.now())
        elif self.value() == 'overdue':
            return queryset.filter(date_due__lt=timezone.now()).exclude(status__in=['F','S'])
        else:
            return queryset

