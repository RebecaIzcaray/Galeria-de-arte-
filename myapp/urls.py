from django.urls import path 
from myapp import views
from .views import crear_obra
from .views import mostrar_obras

urlpatterns = [
    path('', views.hello),
    path('crear-obra/', crear_obra, name='crear_obra'),
    path('mostrar-obras/', mostrar_obras, name='mostrar_obras'),
]