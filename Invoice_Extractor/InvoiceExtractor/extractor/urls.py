from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_invoice, name='upload_invoice'),
    
    
]
