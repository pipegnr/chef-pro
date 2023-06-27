from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#Queremos agregar el campo "email" en el form UserCreationForm, por lo que creamos una nueva class
#que inherits del UserCreationForm, pero con el agregado que queremos.
#Puede tomar un argumento llamado required, que lo deja como llenado obligatorio o no, el default
#está seteado como True.
#Recordemos que Meta nos ayuda a cambiar cosas que vienen por defecto en el Framework.
#Aquí especificamos el modelo con el que se quiere que este form interactúe (User).

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
#En este último definimos el orden y los campos que serán displayed in the form.

################################################################

#Actualización de profile

class UserUpdateForm(forms.ModelForm):   #inherits from forms.ModelForm
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

#Fin de actualización de profile