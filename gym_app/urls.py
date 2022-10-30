from django.urls import path
from . import views

app_name = 'gym'

urlpatterns = [
    path('', views.Index.as_view(), name = 'index'),
    path('checkout/<int:pk>/', views.Checkout.as_view(), name = 'checkout'),
    path('plans/', views.PlansView.as_view(), name = 'plans'),
    path('success/', views.Success.as_view(), name = 'success'),
    path('cancel/', views.CancelView.as_view(), name = 'cancel'),
    path('help/', views.send_email, name = 'help_center'),
    path('about/', views.AboutView.as_view(), name = 'about'),
    path('plan/<slug:slug>', views.PlanView.as_view(), name = 'plan'),
    path('account/', views.AccountView.as_view(), name = 'account'),

]