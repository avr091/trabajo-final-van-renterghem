from django import forms
from django.contrib.auth.models import User



class PistolaFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    fps=forms.IntegerField()

class AsaltoFormulario (forms.Form):
    nombre=forms.CharField(max_length=30)
    tipo=forms.CharField(max_length=30)
    fps=forms.IntegerField()
    imagen =forms.ImageField(required=False)


class DmrFormulario (forms.Form):
    nombre=forms.CharField(max_length=30)
    tipo=forms.CharField(max_length=30)
    fps=forms.IntegerField()

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}