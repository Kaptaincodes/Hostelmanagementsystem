from django.urls import path
from .views import staff_homepage, user_request_edit_admin, change_status, search

urlpatterns = [
    path('', staff_homepage, name='staff_homepage'),
    path('search', search, name='search' ),
    path('<id>/edit/', user_request_edit_admin, name='user_request_edit_admin'),
    path('<id>/change/status/', change_status, name='change_status'),
]
