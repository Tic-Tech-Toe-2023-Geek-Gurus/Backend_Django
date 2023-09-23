from django.urls import path
from .views import *

urlpatterns = [
    path('register/',register_page),
    path('login/',login_page)
]
