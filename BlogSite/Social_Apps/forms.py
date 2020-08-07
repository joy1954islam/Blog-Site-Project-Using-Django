from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from Social_Apps.models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name','last_name','password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        for email in self.fields.keys():
            self.fields[email].widget.attrs.update({
                'class': 'form-control',
            })
    class Meta:
         model = User
         fields = (
                 'email','first_name','last_name'
                )


class ProfileForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.widgets.DateInput(attrs={"type": "date"}))

    # or
    # publication_date = forms.CharField(widget=forms.widgets.DateInput(attrs={"type": "date"}))
    #
    # publication_date = forms.DateField(
    # label='What is your publication date?',
    # # change the range of the years from 1980 to currentYear
    # widget=forms.SelectDateWidget(years=range(1980, datetime.date.today().year))
    # )

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for nickname in self.fields.keys():
            self.fields[nickname].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Profile
        fields = [
            'nickname','dob','gender','bio','profile_image'
        ]

