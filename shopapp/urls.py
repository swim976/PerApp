from django.urls import path
from . import views

urlpatterns = [
    path('address', views.save_address, name='address'),
    path('address_test', views.address_test, name='address_test')
]