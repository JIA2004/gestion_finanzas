from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('investment/create/', views.investment_create, name='investment_create'),
    path('saving/create/', views.saving_create, name='saving_create'),
    path('income/create/', views.income_create, name='income_create'),
    path('expense/create/', views.expense_create, name='expense_create'),
    # Agrega más URLs según sea necesario
]

# Añade esta línea para el registro
urlpatterns += [
    path('signup/', views.signup, name='signup'),
]
