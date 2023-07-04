from django.urls import path
from kickbox_academy.core import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('register/', views.register_page, name='register')
]