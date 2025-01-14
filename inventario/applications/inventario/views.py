from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .forms import InventarioForm
from .models import Inventario

# Create your views here.

class InventarioCreateView(CreateView):
    form_class = InventarioForm
    template_name = "inventario/add-inventario.html"
    success_url = "."


class InventarioListView(ListView):
    template_name = "inventario/lista-inventario.html"
    context_object_name = "lista"
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super(InventarioListView, self).get_context_data(**kwargs)
        
        context["inventarios"] = Inventario.objects.all()

        return context
    
    def get_queryset(self):
        return []
    

class InventarioDetailView(DetailView):
    model = Inventario
    template_name = "inventario/detail-inventario.html"
    context_object_name = "equipo"
