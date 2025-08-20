from django.urls import path
from . import views
from .views import proxy_api


urlpatterns = [
    path('', views.index, name='home'),  # Ruta raíz
    path("proxy/api/", proxy_api, name="proxy_api"),
]
