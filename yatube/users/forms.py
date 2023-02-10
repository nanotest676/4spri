from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class ContactForm(forms.Form):
    first_name = forms.CharField(label='Введите имя', initial='Лев')
    last_name = forms.CharField(label='Введите фамилию', initial='Толстой')
