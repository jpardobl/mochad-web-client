from django.contrib import admin
from web.models import *


class DeviceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Device, DeviceAdmin)


class X10CommandAdmin(admin.ModelAdmin):
    pass
admin.site.register(X10Command, X10CommandAdmin)
