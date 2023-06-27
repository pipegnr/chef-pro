from django.contrib import admin
from django.urls import path
from . import views
from .views import OcListView, OcDetailView

urlpatterns = [
    path('crear_oc/', views.crear_oc, name='compras-crear_oc'),
    path('oc_listado/', OcListView.as_view(), name='compras-oc_listado'),
    path('oc_detalle/<int:pk>/', OcDetailView.as_view(), name='compras-oc_detalle'),
    path('crear_proveedor/', views.crear_proveedor, name='compras-crear_proveedor'),
    path('oc_detalle/<int:pk>/registro_recepciones/', views.registro_recepciones, name='registro_recepciones'),

]