from django import forms
from django.forms import inlineformset_factory
from .models import Gramajes, Receta, Materia_prima


class CrearMPForm(forms.ModelForm):
    class Meta:
        model = Materia_prima
        fields = ['descripcion', 'categoria', 'descripcion', 'categoria', 'subcategoria', 'unidad_de_medida','merma',\
'calorias', 'carbohidratos', 'proteina', 'sodio', 'azucares', 'grasa_total', 'grasa_saturada', \
'grasa_monosaturada', 'grasa_poliinsaturada', 'grasa_trans', 'colesterol', 'fibras']

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if Materia_prima.objects.filter(descripcion__iexact=descripcion).exists():
            raise forms.ValidationError('Este ingrediente ya existe en la base de datos.')
        return descripcion




#SECCIÓN: CREACIÓN DE RECETA
    #Lo siguiente es para un form de nombre de receta (model Receta), junto a tabla Gramajes que incluye
    #Materia_prima y cantidad de materia prima como un additional field.
class MateriaPrimaForm(forms.ModelForm):
    class Meta:
        model = Materia_prima
        fields = ['descripcion']


class RecetaForm(forms.Form):
    nombre_receta = forms.CharField(max_length=45, label='Nombre receta')

    class Meta:
        model = Receta
        fields = ['nombre_receta']

class GramajesForm(forms.ModelForm):
    class Meta:
        model = Gramajes
        exclude = ()

GramajesFormset = inlineformset_factory(Receta, Gramajes, form=GramajesForm, extra=2, can_delete=False)
#FIN SECCIÓN: CREACIÓN DE RECETA

