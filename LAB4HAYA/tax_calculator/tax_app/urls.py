from django.urls import path
from . import views

urlpatterns = [
    path('', views.default, name='default'),
    path('<int:number>/', views.calculate_tax, name='calculate_tax'),
    path('tax_rate/', views.tax_rate_view, name='tax_rate_view'),
]
