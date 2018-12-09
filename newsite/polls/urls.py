from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, {'lol': ' PIDOTA!', 'test': ' SUKA!'}, name='index'),
]
