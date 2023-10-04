from django.urls import path
from . import views

app_name = 'banking_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('forms', views.forms, name='forms'),
    path('get_districts_and_branches', views.get_districts_and_branches, name='get_districts_and_branches'),
   
]
  