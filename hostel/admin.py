from django.contrib import admin
from .models import Hostel


class HostelAdmin(admin.ModelAdmin):
    list_display = ('__str__','total_bedspace', 'total_available_bedspace', 'total_booked_bedspace')


admin.site.register(Hostel, HostelAdmin)
