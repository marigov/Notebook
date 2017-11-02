from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateNoteForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(max_length=2000)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required.')
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    username = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class NotesSearchForm(forms.Form):
    search_text = forms.CharField(
        required=False,
        label='Search',
        # widget=forms.TextInput(attrs={'placeholder': 'search here!'})
    )

