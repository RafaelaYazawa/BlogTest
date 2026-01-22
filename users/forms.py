from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length = 100,
        required=False,
        help_text = 'This field is optional and can be set up in the profile page',
        widget = forms.TextInput(attrs={ 'id': 'first_name', 'class': 'bg-neutral-secondary-medium border border-default-medium text-heading rounded-xl focus:ring-brand focus:border-brand block w-full px-3 py-2.5 shadow-xs placeholder:text-neutral-500', 'placeholder': 'First name (optional)'})
    )
    last_name = forms.CharField(
        max_length = 100,
        required = False,
        help_text='This field is optional and can be set up in the profile page',
        widget = forms.TextInput(attrs={ 'id': 'last_name', 'class': 'bg-neutral-secondary-medium border border-default-medium text-heading rounded-xl focus:ring-brand focus:border-brand block w-full px-3 py-2.5 shadow-xs placeholder:text-neutral-500', 'placeholder': 'Last name (optional)'})
    )
    email = forms.EmailField(
        max_length = 100,
        required = True,
        help_text = 'Enter a valid email address.',
        widget = forms.TextInput(attrs={'id': 'email' ,'class': 'bg-neutral-secondary-medium border border-default-medium text-heading rounded-xl focus:ring-brand focus:border-brand block w-full px-3 py-2.5 shadow-xs placeholder:text-neutral-500', 'placeholder': 'Email'})
    )
    username = forms.CharField(
        max_length = 200,
        required = True,
        help_text = 'Enter a valid username',
        widget = forms.TextInput(attrs={ 'id': 'username', 'class': 'bg-neutral-secondary-medium border border-default-medium text-heading rounded-xl focus:ring-brand focus:border-brand block w-full px-3 py-2.5 shadow-xs placeholder:text-neutral-500', 'placeholder': 'Username'})
    )
    password1 = forms.CharField(
        help_text = 'Enter a password',
        required = True,
        widget = forms.TextInput(attrs={ 'id': 'password1', 'class': 'bg-neutral-secondary-medium border border-default-medium text-heading rounded-xl focus:ring-brand focus:border-brand block w-full px-3 py-2.5 shadow-xs placeholder:text-neutral-500', 'placeholder': '********'})
    )
    password2 = forms.CharField(
        help_text = 'Repeat your password',
        required = True,
        widget = forms.TextInput(attrs={ 'id': 'password2', 'class': 'bg-neutral-secondary-medium border border-default-medium text-heading rounded-xl focus:ring-brand focus:border-brand block w-full px-3 py-2.5 shadow-xs placeholder:text-neutral-500', 'placeholder': '********'})
    )

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username', 'email', 'password1', 'password2'
        ]