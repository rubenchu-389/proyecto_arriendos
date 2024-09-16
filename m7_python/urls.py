from django.urls import path
from m7_python.views import index, register, profile, change_pass

urlpatterns =[
    path ('', index, name='index'),
    path('accounts/register/', register, name='register'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/change-pass/', change_pass, name='change_pass'),
    
]




