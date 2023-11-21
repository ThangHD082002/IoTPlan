from django.contrib import admin
from .models import Sensor
from django.contrib import messages
from django.utils.translation import ngettext
from django.utils.translation import gettext_lazy as _


# Register your models here.

class SensorAdmin(admin.ModelAdmin):
    readonly_fields = ('time', )

    sortable_by = ('time', )

    def __init__(self, model, admin_site):
        self.form.admin_site = admin_site
        super(SensorAdmin, self).__init__(model, admin_site)


# Registers the article model at the admin backend.
admin.site.register(Sensor, SensorAdmin)