from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm
from .models import Perfil

class ProfileForm(ModelForm):
    class Meta:
        model = Perfil
        exclude = ('es_moderador',)
