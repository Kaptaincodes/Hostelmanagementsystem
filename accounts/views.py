from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

from django.contrib.auth.models import User
from django.contrib import messages 
from .models import UserProfile

from .forms import UserLoginForm, UserRegisterForm


#LOGIN METHOD
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'Invalid Matric Number or password')
            return redirect('login')
    else:
        return render(request, "registration/login.html",)


#REGISTER METHOD
def register_view(request):
    if request.method == 'POST':
        #Get form values
        first_name =  request.POST['first_name']
        last_name =  request.POST['last_name']
        username =  request.POST['username']
        email =  request.POST['email']
        password =  request.POST['password']
        password2 =  request.POST['password2']
        gender =  request.POST['gender']

        # check if password match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'The Matric Number is registered already')
                return redirect('register')

            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'The Matric Number is being use')
                    return redirect('register')
                else:
                    #register a user
                    user = User.objects.create_user(username=username, password=password, email=email, last_name=last_name, first_name=first_name,)
                    user.save()
                    profile = UserProfile.objects.create(user=user, gender=gender)
                    profile.user = user
                    profile.save()


                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')

        else:
            messages.error(request, 'Passwords Do not Match')
            return redirect('register')
    else:
        return render(request, "registration/register.html",)

def logout(request):
    
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('homepage')






# FORM LOGIN 

"""     next = request.GET.get('next'),
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username= form.cleaned_data.get('username')
        password= form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')
    context = {
        'form': form
    } """