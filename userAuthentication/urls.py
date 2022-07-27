from django.urls import path, include
from django.contrib.auth import views as auth_views
from userAuthentication.views import edit

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('social_django.urls', namespace='social')),
    path('edit/', edit, name='edit'),
]