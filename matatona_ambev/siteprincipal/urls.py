from django.urls import path, include

from .views import home

app_name = 'landpage'
urlpatterns = [
    path('', home, name='home'),
    path('comprador', include('comprador.urls')),
]
