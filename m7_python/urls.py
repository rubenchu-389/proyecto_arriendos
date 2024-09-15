from django.urls import path
from m7_python.views import index, register

urlpatterns =[
    path ('', index, name='index'),
    path('accounts/register/', register, name='register'),
    ]




