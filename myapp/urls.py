from django.urls import path
from .views import transfer_form

urlpatterns = [
    path('', transfer_form),
]