from django.urls import path
from . import views

app_name = 'gym'

urlpatterns = [
    path('', views.Index.as_view(), name = 'index'),
    path('checkout/<int:pk>/', views.Checkout.as_view(), name = 'checkout'),
    path('success/', views.Success.as_view(), name = 'success'),
    path('cancel/', views.CancelView.as_view(), name = 'cancel')
]