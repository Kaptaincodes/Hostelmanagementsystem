from django.contrib import admin
from .models import Visitor, BookingInfo
from visitor.forms import BookingInfoInlineAdminForm, VisitorAdminForm


class BookingInfoInline(admin.StackedInline):
    model = BookingInfo
    form = BookingInfoInlineAdminForm

    def get_extra(self, request, obj=None, **kwargs):
        return 1


class VisitorAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'room_number', 'status', 'date_of_booking','is_departed','hostel_name')
    inlines = [BookingInfoInline]
    form = VisitorAdminForm
    fields = (
        'user',
        'room_number',
        'date_of_booking',
        'room_preference',
        'status',
        'is_departed',
        'hostel_name',
    )


admin.site.register(Visitor, VisitorAdmin)
