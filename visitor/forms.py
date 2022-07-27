from django import forms
from visitor.models import Visitor
from visitor.util import total_rooms
from django.utils import timezone
from .util import get_zip_hostel_room
import itertools


class BookARoom(forms.ModelForm):
    """
    form for booking rooms.
    """

    class Meta:
        model = Visitor
        fields = ['hostel_name','room_number','room_preference',]
        widgets = {

            'hostel_name': forms.Select(attrs=({
                'class': 'form-control'
            })),

            'room_number': forms.TextInput(attrs=({
                'class': 'form-control'
            })),
            'room_preference': forms.Select(attrs=({
                'class': 'form-control'
            })),
        }



class BookingInfoInlineAdminForm(forms.ModelForm):
    def clean(self):
        room, hostel, type = get_zip_hostel_room(self.cleaned_data.get('visitor'))
        room_get = self.cleaned_data.get('room_number')
        hostelname_get = self.cleaned_data.get('hostel_name')
        hostel_get = self.cleaned_data.get('hostel_allotted')
        type_get = self.cleaned_data.get('room_preference')
        print(room_get, hostel_get, type_get)
        # for h, r in l:
        #     if str(h) == str(hostel) and str(r) == str(room):
        #         raise forms.ValidationError("Room Already Allotted")
        for r, h, t in itertools.zip_longest(room, hostel, type):
            if str(r) == str(room_get) and str(h) == str(hostel_get) and str(t) == str(type_get):
                raise forms.ValidationError("Room Already Allotted")
        return self.cleaned_data


class VisitorAdminForm(forms.ModelForm):
    def clean(self):
        # is_arrived = self.cleaned_data.get('is_arrived')
        status = self.cleaned_data.get('status')
        is_departed = self.cleaned_data.get('is_departed')
        # if is_arrived and status is False:
        #     raise forms.ValidationError("Booking Is Not Confirmed Yet")
        # elif is_departed and status is False:
        #     raise forms.ValidationError("Booking Is Not Confirmed Yet")
        # elif is_departed and is_arrived is False:
        #     raise forms.ValidationError("Visitor Hasn't Arrived Yet")
        # return self.cleaned_data
        if not status and is_departed:
            raise forms.ValidationError("Booking Not Confirmed Yet")
        return self.cleaned_data
