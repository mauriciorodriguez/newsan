from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from TestNewsan.constant import FILTRO_DESCRIPCION, FILTRO_ESTADO, FILTRO_ID, OBJETO_TODOS_TEMPLATE
from todoapp.models import Todo

class TodoCreateView(CreateView):
    model = Todo
    fields = ["descripcion", "adjunto"]
    template_name = "crear_todo.html"

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "borrar_todo.html"
    success_url = reverse_lazy("listar-todo")

class TodoUpdateView(UpdateView):
    model = Todo
    fields = "__all__"
    template_name = "editar_todo.html"    

class TodoListView(ListView):
    model = Todo
    queryset = Todo.objects.all()
    context_object_name = OBJETO_TODOS_TEMPLATE
    template_name = "listar_todo.html"
    
class TodoPorIDListView(ListView):
    model = Todo
    template_name = "id_todo.html"
    def get_context_data(self):
        context = super().get_context_data()
        try:
            context["todo"] = Todo.objects.get(pk=self.request.GET[FILTRO_ID])
        except Todo.DoesNotExist:
            pass
        return context
    
class TodoPorEstadoListView(ListView):
    model = Todo  
    template_name = "listar_todo.html"
    def get_context_data(self):
        context = super().get_context_data()
        context[OBJETO_TODOS_TEMPLATE] = Todo.objects.filter(estado=self.request.GET[FILTRO_ESTADO])
        return context

class TodoPorDescripcionListView(ListView):
    model = Todo
    template_name = "listar_todo.html"
    def get_context_data(self):
        context = super().get_context_data()
        context[OBJETO_TODOS_TEMPLATE] = Todo.objects.filter(descripcion=self.request.GET[FILTRO_DESCRIPCION])
        return context
    

    


