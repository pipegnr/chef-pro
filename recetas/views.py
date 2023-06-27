from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Categoria_material, Unidad_de_medida, Receta, Materia_prima
from django.views.generic import ListView, DetailView
from django.db.models import Sum
from .forms import CrearMPForm, RecetaForm, GramajesFormset
from django.contrib import messages


def home(request):
    if request.user.is_authenticated:
        return render(request, 'recetas/base.html')
    else:
        return redirect('login')


def crear_mp(request):

    if request.method == "POST":
        form = CrearMPForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha creado una nueva Materia Prima')
            if 'create_another' in request.POST:
                return redirect('recetas-crear_mp')
            return redirect('recetas-home')
        else:
            #messages.error(request, 'Ha ocurrido un error (Flag 1). Contacte a su administrador.')
            for field, errors in form.errors.items():
                for error in errors:
                    messages.warning(request, f"{error}")
                    return redirect('recetas-home')

    else:
        form = CrearMPForm()
        return render(request, "recetas/crear_mp.html", {"form": form})

def crear_categoria_um(request):
    categorias = Categoria_material.objects.all()
    unidades_de_medida = Unidad_de_medida.objects.all()
    context = {
        'categorias': categorias,
        'unidades_de_medida': unidades_de_medida
    }
    return render(request, 'recetas/crear_categoria_um.html', context)

def crear_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST)
        formset = GramajesFormset(request.POST, prefix='ingredientes')
        if form.is_valid() and formset.is_valid():
            receta = Receta.objects.create(nombre_receta=form.cleaned_data['nombre_receta'])
            formset.instance = receta
            formset.save()
            messages.success(request, 'Se ha creado una nueva Receta')
            if 'create_another' in request.POST:
                return redirect('recetas-crear_receta')
            return redirect('recetas-recetas_listado')
        else:
            #messages.error(request, 'Ha ocurrido un error (Flag 1). Contacte a su administrador.')
            for field, errors in form.errors.items():
                for error in errors:
                    messages.warning(request, f"{error}")
                    return redirect('recetas-home')
    else:
        form = RecetaForm()
        formset = GramajesFormset(prefix='ingredientes')
    return render(request, 'recetas/crear_receta.html', {'form': form, 'formset': formset})

class RecetasListView(ListView):
    model = Receta
    template_name = 'recetas/recetas_listado.html'
    context_object_name = 'recetas'

class RecetasDetailView(DetailView):
    model = Receta
    template_name = 'recetas/recetas_detalle.html'

    #Lo siguiente es necesario para pasar más variables en el context, y son las sumas de cada componente nutricional.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   #Primero, el damos el valor por default a context.
        receta = self.get_object()     #Llamamos al objeto, y comenzamos a darle los valores totales como si fuese un diccionario.

        calorias_totales = receta.ingredientes.aggregate(sum_quantity=Sum('calorias'))
        context['calorias_totales'] = calorias_totales['sum_quantity']
        carbohidratos_totales = receta.ingredientes.aggregate(sum_quantity=Sum('carbohidratos'))
        context['carbohidratos_totales'] = carbohidratos_totales['sum_quantity']
        proteina_totales = receta.ingredientes.aggregate(sum_quantity=Sum('proteina'))
        context['proteina_totales'] = proteina_totales['sum_quantity']
        sodio_totales = receta.ingredientes.aggregate(sum_quantity=Sum('sodio'))
        context['sodio_totales'] = sodio_totales['sum_quantity']
        azucares_totales = receta.ingredientes.aggregate(sum_quantity=Sum('azucares'))
        context['azucares_totales'] = azucares_totales['sum_quantity']
        grasa_total_totales = receta.ingredientes.aggregate(sum_quantity=Sum('grasa_total'))
        context['grasa_total_totales'] = grasa_total_totales['sum_quantity']
        grasa_saturada_totales = receta.ingredientes.aggregate(sum_quantity=Sum('grasa_saturada'))
        context['grasa_saturada_totales'] = grasa_saturada_totales['sum_quantity']
        grasa_monosaturada_totales = receta.ingredientes.aggregate(sum_quantity=Sum('grasa_monosaturada'))
        context['grasa_monosaturada_totales'] = grasa_monosaturada_totales['sum_quantity']
        grasa_poliinsaturada_totales = receta.ingredientes.aggregate(sum_quantity=Sum('grasa_poliinsaturada'))
        context['grasa_poliinsaturada_totales'] = grasa_poliinsaturada_totales['sum_quantity']
        grasa_trans_totales = receta.ingredientes.aggregate(sum_quantity=Sum('grasa_trans'))
        context['grasa_trans_totales'] = grasa_trans_totales['sum_quantity']
        colesterol_totales = receta.ingredientes.aggregate(sum_quantity=Sum('colesterol'))
        context['colesterol_totales'] = colesterol_totales['sum_quantity']
        fibras_totales = receta.ingredientes.aggregate(sum_quantity=Sum('fibras'))
        context['fibras_totales'] = fibras_totales['sum_quantity']

        return context
    


class Materia_primaListView(ListView):
    model = Materia_prima
    template_name = 'recetas/mp_listado.html'
    context_object_name = 'materias_primas'


class Materia_primaDetailView(DetailView):
    model = Materia_prima
    template_name = 'recetas/mp_detalle.html'
