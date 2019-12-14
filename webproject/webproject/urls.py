
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('psynora/',views.index),
    path('admin/', admin.site.urls),
]
