from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from visitor.forms import BookARoom
from visitor.util import total_rooms
from visitor.models import Visitor, BookingInfo
from django.utils import timezone
from userAuthentication.forms import EditRequests
from django.http import HttpResponseRedirect


@login_required
def homepage(request):
    """
    home page for users.
    """
    if request.user.is_staff:
        return HttpResponseRedirect(reverse('staff_homepage'))
    booking_info = BookingInfo.objects.filter(visitor__user=request.user).filter(visitor__is_departed=False)
    current_request = Visitor.objects.filter(user=request.user).filter(is_departed=False).first()
    rooms = total_rooms()
    if request.method == "POST":
        form = BookARoom(request.POST)
        if current_request:
            return HttpResponseRedirect(reverse('homepage'))
        if form.is_valid():
            required_rooms = form.cleaned_data.get('room_number')
            hostelname_name = form.cleaned_data.get('hostel_name')
            Visitor.objects.create(user=request.user, room_number=required_rooms,hostel_name=hostelname_name,
                                   date_of_booking=timezone.now())
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = BookARoom()
    return render(request, 'homepage/home.html',
                  {'form': form, 'current_request': current_request,
                   'booking_info': booking_info, 'rooms': rooms})


@login_required()
def edit(request):
    """
    page for editing the existing request for the user.
    """
    try:
        visitor = Visitor.objects.filter(user=request.user).filter(is_departed=False).first()
    except Visitor.DoesNotExist:
        return HttpResponseRedirect(reverse('homepage'))
    if visitor.status:
        HttpResponseRedirect(reverse('homepage'))
    current_request = Visitor.objects.filter(user=request.user).filter(is_departed=False).first()
    if current_request:
        if request.method == 'POST':
            form = EditRequests(request.POST)
            if form.is_valid():
                visitor.room_number = form.cleaned_data.get('room_number')
                visitor.room_preference = form.cleaned_data.get('room_preference')
                visitor.save(update_fields=['room_number', 'room_preference'])
                return HttpResponseRedirect(reverse('homepage'))
        else:
            initial_data = {
                'room_number': visitor.room_number,

                'room_preference': visitor.room_preference,
            }
            form = EditRequests(initial=initial_data)
        return render(request, 'homepage/edit.html', {'form': form})
