from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/django_hash_make_password', views.django_hash_make_password, name='django_hash_make_password'),
]
