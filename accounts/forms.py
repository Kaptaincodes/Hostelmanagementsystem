from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,

)

GENDER_CHOICES = [
    ('male','MALE'),
    ('female','FEMALE'),
]

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('This password is incorrect')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    gender = forms.CharField(max_length=6, widget=forms.Select(choices=GENDER_CHOICES),)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'gender', 
        ]

    def clean_email(self):
        email = self.cleaned_data.get(email)
        email_qs = User.objects.fileter(email)
        if email_qs.exist():
            raise forms.ValidationError("This emails is already being used")
        return email
