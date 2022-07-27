from django.shortcuts import render, redirect
from visitor.models import Visitor, BookingInfo
from django.contrib.auth import get_user_model
from staffUser.forms import BooingAdminPanelForm, booking_admin_panel_inline_form_base_form_set
from django import forms
from hostel.models import Hostel
from django.urls import reverse
from django.http import HttpResponseRedirect, request
from visitor.choices import search_choices
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages


User = get_user_model()


def staff_homepage(request):
    """
    Homepage for staff users.
    """
    visitor = Visitor.objects.all().order_by('-date_of_booking')

    paginator = Paginator(visitor, 5)
    page = request.GET.get('page')
    paged_visitor = paginator.get_page(page)
    context= {
        'visitor': paged_visitor, 
        'search_choices':search_choices
    }
    return render(request, 'staffUser/index.html', context)

def search(request):
    
    # queryset_list = Visitor.objects
    

    queryset_list = Visitor.objects.all().order_by('-date_of_booking')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
             queryset_list =  queryset_list.filter(hostel_name__iexact=keywords)

    paginator = Paginator(queryset_list, 5)
    page = request.GET.get('page')
    paged_visitor = paginator.get_page(page)

    context= {
        'visitor':  paged_visitor, 
        'search_choices':search_choices
    }
    return render(request, 'staffUser/search.html', context)


def user_request_edit_admin(request, id):
    """
    Page for editing user requests in the admin panel.
    """
    user = User.objects.get(pk=id)
    visitor_obj = Visitor.objects.filter(user=user).order_by('-date_of_booking').first()
    BookingAdminPanelInlineFormSet = forms.inlineformset_factory(Visitor, BookingInfo, form=BooingAdminPanelForm,
                                                                 can_delete=True,
                                                                 max_num=1,
                                                                 
                                                                
                                                                  formset=booking_admin_panel_inline_form_base_form_set,
                                                                 )
                                                                #  no_of_rooms_required
        
    if request.method == 'POST':
        form = BookingAdminPanelInlineFormSet(request.POST, instance=visitor_obj)
        if form.is_valid():
            form.save()
    else:
        form = BookingAdminPanelInlineFormSet(instance=visitor_obj)
    return render(request, 'staffUser/edit.html', {'visitor_obj': visitor_obj, 'form': form,})


def change_status(request, id):
    """
    - Update total available rooms in each hostel in database
    - Change the status of the user to True, i.e. booking confirmed.
    """
    visitor_obj = Visitor.objects.get(pk=id)
    # books = BookingInfo.objects.get(pk=id)

    IBH = Hostel.objects.get(name__iexact='IBH')
    JAH = Hostel.objects.get(name__iexact='JAH')
    DLW = Hostel.objects.get(name__iexact='DLW')
    UFH = Hostel.objects.get(name__iexact='UFH')
    booking_info = BookingInfo.objects.filter(visitor=visitor_obj)
    if not visitor_obj.status:
        for info in booking_info:
            if info.room_number == '0000' and info.hostel_allotted == '0':
                raise forms.ValidationError('Please Fill The Form')
            hostel_allotted = info.hostel_allotted
            if hostel_allotted == '1':
                
                if IBH.total_booked_bedspace < IBH.total_bedspace:
                    IBH.total_available_bedspace -= 1
                    IBH.total_booked_bedspace += 1 
                    IBH.save()
                       
                else:
                    messages.error(request, 'Hostel is filled up')
                    return HttpResponseRedirect(reverse('user_request_edit_admin', args=[visitor_obj.user.id]))

            elif hostel_allotted == '2':
                if JAH.total_booked_bedspace < JAH.total_bedspace:
                    JAH.total_available_bedspace -= 1
                    JAH.total_booked_bedspace += 1 
                    JAH.save()
                       
                else:
                    messages.error(request, 'Hostel is filled up')
                    return HttpResponseRedirect(reverse('user_request_edit_admin', args=[visitor_obj.user.id]))

            elif hostel_allotted == '3':

                if DLW.total_booked_bedspace < DLW.total_bedspace:
                    DLW.total_available_bedspace -= 1
                    DLW.total_booked_bedspace += 1 
                    DLW.save()
                       
                else:
                    messages.error(request, 'Hostel is filled up')
                    return HttpResponseRedirect(reverse('user_request_edit_admin', args=[visitor_obj.user.id]))
            
            elif hostel_allotted == '4':

                if UFH.total_booked_bedspace < UFH.total_bedspace:
                    UFH .total_available_bedspace -= 1
                    UFH.total_booked_bedspace += 1 
                    UFH.save()
                       
                else:
                    messages.error(request, 'Hostel is filled up')
                    return HttpResponseRedirect(reverse('user_request_edit_admin', args=[visitor_obj.user.id]))

        visitor_obj.is_departed = False
        visitor_obj.status = True
        visitor_obj.room_number = info.room_number
        visitor_obj.hostel_name = info.hostel_name
        visitor_obj.room_preference = info.room_preference
        visitor_obj.save()
    else:
        if visitor_obj.status:
            if not visitor_obj.is_departed:
                visitor_obj.is_departed = True
                visitor_obj.save()
        for info in booking_info:
            hostel_allotted = info.hostel_allotted
            print(hostel_allotted)
            if hostel_allotted == '1':
                IBH.total_available_bedspace += 1
                IBH.total_booked_bedspace -= 1
                IBH.save()
            elif hostel_allotted == '2':
                JAH.total_available_bedspace += 1
                JAH.total_booked_bedspace -= 1
                JAH.save()
            elif hostel_allotted == '3':
                DLW.total_available_bedspace += 1
                DLW.total_booked_bedspace -= 1
                DLW.save()
            
            elif hostel_allotted == '4':
                UFH.total_available_bedspace += 1
                UFH.total_booked_bedspace -= 1
                UFH.save()
        visitor_obj.status = False
        visitor_obj.save()
    return HttpResponseRedirect(reverse('user_request_edit_admin', args=[visitor_obj.user.id]))
