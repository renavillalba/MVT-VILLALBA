from django.contrib import admin
from django.urls import path
from Familiares.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mensaje/', intro_message),
    path('familia/', integrantes),
]
