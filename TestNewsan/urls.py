"""TestNewsan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from todoapp.views import TodoCreateView, TodoDeleteView, TodoListView, TodoPorDescripcionListView, TodoPorEstadoListView, TodoPorIDListView, TodoUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("crear/", TodoCreateView.as_view(),name="crear-todo"),
    path("", TodoListView.as_view(),name="listar-todo"),
    path("editar/<int:pk>", TodoUpdateView.as_view(),name="editar-todo"),
    path("borrar/<int:pk>", TodoDeleteView.as_view(),name="borrar-todo"),
    path("filtro/id", TodoPorIDListView.as_view()),
    path("filtro/estado", TodoPorEstadoListView.as_view()),
    path("filtro/descripcion", TodoPorDescripcionListView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
