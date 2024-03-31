from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home_page'),
    path('api/django_hash_make_password', views.django_hash_make_password, name='django_hash_make_password'),
    path('api/django_hash_check_password', views.django_hash_check_password, name='django_hash_check_password'),
]
