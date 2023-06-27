from django.contrib import admin
from django.urls import path
from . import views
from .views import RecetasListView, RecetasDetailView, Materia_primaListView, Materia_primaDetailView

urlpatterns = [
    path('', views.home, name='recetas-home'),
    path('crear_categoria_um/', views.crear_categoria_um, name='recetas-crear_categoria_um'),
    path('crear_mp/', views.crear_mp, name='recetas-crear_mp'),
    path('crear_receta/', views.crear_receta, name='recetas-crear_receta'),
    path('recetas_listado/', RecetasListView.as_view(), name='recetas-recetas_listado'),
    path('recetas_detalle/<int:pk>/', RecetasDetailView.as_view(), name='recetas-receta_detalle'),
    path('mp_listado/', Materia_primaListView.as_view(), name='recetas-mp_listado'),
    path('mp_detalle/<int:pk>/', Materia_primaDetailView.as_view(), name='recetas-mp_detalle'),
]