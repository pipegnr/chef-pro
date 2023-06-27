from django.shortcuts import render, redirect
from .models import Orden_de_compra, Mp_Oc, Recepcion
from recetas.models import Materia_prima
from .forms import Orden_de_compraForm, Mp_OcFormset, ProveedorForm
from django.contrib import messages
from django.views.generic import ListView, DetailView
from decimal import Decimal
from django.http import HttpResponse




def crear_oc(request):

    if request.method == 'POST':
        form = Orden_de_compraForm(request.POST)
        formset = Mp_OcFormset(request.POST, prefix='materias_primas')
        if form.is_valid() and formset.is_valid():
            proveedor = form.cleaned_data.get('proveedor')
            orden_de_compra = Orden_de_compra.objects.create(proveedor=proveedor)
            formset.instance = orden_de_compra
            formset.save()
            messages.success(request, 'Se ha creado una nueva Orden de Compra')
            if 'create_another' in request.POST:
                return redirect('compras-crear_oc')
            return redirect('compras-oc_listado')
        else:
            return redirect('compras-oc_listado')

    else:
        form = Orden_de_compraForm()
        formset = Mp_OcFormset(prefix='materias_primas')
    return render(request, 'compras/crear_oc.html', {'form': form, 'formset': formset})


class OcListView(ListView):
    model = Orden_de_compra
    template_name = 'compras/oc_listado.html'
    context_object_name = 'ordenes_de_compra'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ordenes_de_compra_list'] = [
            {
                'orden': orden,
                'precio_neto_oc': orden.precio_neto_oc,  # access the property here
            }
            for orden in context['ordenes_de_compra']
        ]
        return context


class OcDetailView(DetailView):
    model = Orden_de_compra
    template_name = 'compras/oc_detalle.html'
    context_object_name = 'orden_de_compra'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #Pasamos la data de cada línea de la OC
        context['materias_primas'] = Mp_Oc.objects.filter(nro_oc=self.object).select_related('materia_prima')
        #Lo siguiente para pasar el valor del IVA.

#test para pdtes recepcion
        mp_oc_queryset = Mp_Oc.objects.filter(nro_oc=self.object).select_related('materia_prima')
        recepcion_queryset = Recepcion.objects.filter(nro_oc=self.object).select_related('materia_prima')

        
        
        pendientes = {}

        # Fetch the related Materia_prima objects and their inventario values
        for mp_oc in mp_oc_queryset:
            for recepcion in recepcion_queryset:
                pendientes[mp_oc.pk] = mp_oc.cantidad - recepcion.cantidad_recepcion

        # Include the inventario data in the context
        context['inventario'] = pendientes

#fin test

        oc = self.get_object()
        context['items'] = oc.items.all()
        context['iva'] = oc.precio_neto_oc * Decimal(0.19)
        context['total_bruto'] = oc.precio_neto_oc + context['iva']


        return context



def crear_proveedor(request):

    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nuevo proveedor creado!')
            if 'create_another' in request.POST:
                return redirect('compras-crear_proveedor')
            return redirect('recetas-home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.warning(request, f"{error}")
    else:
        form = ProveedorForm()

    return render(request, 'compras/crear_proveedor.html', {'form': form})


def registro_recepciones(request, pk):  #pk es el id de la OC que se está recepcionando.
    nro_oc = Orden_de_compra.objects.get(nro_oc=pk)
    lineas_oc = Mp_Oc.objects.filter(nro_oc=nro_oc)
    
    if request.method == 'POST':
        for linea in lineas_oc:   #es cada linea de Mp_Oc.
            cantidad_recepcion = request.POST.get(f'cantidad_recepcion_{linea.nro_oc}')
            
            #return HttpResponse(linea.pk)    #DEBUGGER FLAG
            #return HttpResponse(cantidad_recepcion) #DEBUGGER FLAG
            #return HttpResponse(linea.materia_prima) #DEBUGGER FLAG
            #return HttpResponse(linea.materia_prima.pk) #DEBUGGER FLAG

            materia_prima = Materia_prima.objects.get(pk=linea.materia_prima.pk)  # Obtiene la instancia de materia prima, según su pk.
            materia_prima.inventario = materia_prima.inventario + Decimal(cantidad_recepcion)  # Se suma lo recepcionado
            materia_prima.save()

            recepcion = Recepcion(
                nro_oc=nro_oc,
                materia_prima=linea.materia_prima,
                cantidad_recepcion=cantidad_recepcion
            )
            recepcion.save()

        return redirect('compras-oc_detalle', pk=pk)



