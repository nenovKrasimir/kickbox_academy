from django.urls import path
from kickbox_academy.core import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('join_academy/', views.join_us_page, name='join_us'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.registration_page, name='register'),
]