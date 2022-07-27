from django import forms
from visitor.models import Visitor
from django.utils import timezone
from visitor.util import total_rooms


class EditRequests(forms.ModelForm):
    """
    Form for editing the current request for the user.
    """
    class Meta:
        model = Visitor
        fields = ['hostel_name','room_number', 'room_preference',]
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


