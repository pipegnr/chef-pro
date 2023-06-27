from django import forms
from django.forms import inlineformset_factory
from .models import Orden_de_compra, Mp_Oc, Proveedor, Recepcion


class Orden_de_compraForm(forms.ModelForm):

    class Meta:
        model = Orden_de_compra
        fields = ['proveedor', 'comentario']

class Mp_OcForm(forms.ModelForm):
    class Meta:
        model = Mp_Oc
        exclude = ()

Mp_OcFormset = inlineformset_factory(Orden_de_compra, Mp_Oc, form=Mp_OcForm, extra=2, can_delete=False)

class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        exclude = ()





