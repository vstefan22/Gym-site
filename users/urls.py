from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name = 'register'),
    path('login/', views.LoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
]