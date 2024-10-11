from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('finanzas.urls')),  # Asume que todas las URLs de la app están en finanzas.urls
]
