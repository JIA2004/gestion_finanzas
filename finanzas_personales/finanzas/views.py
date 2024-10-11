from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Investment, Saving, Income, Expense
from .forms import InvestmentForm, SavingForm, IncomeForm, ExpenseForm, SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

from .services import obtener_precio_actual

@login_required
def dashboard(request):
    investments = Investment.objects.filter(user=request.user)
    savings = Saving.objects.filter(user=request.user)
    incomes = Income.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user)
    
    for investment in investments:
        investment.precio_actual = obtener_precio_actual(investment.ticker)
        investment.save()

    context = {
        'investments': investments,
        'savings': savings,
        'incomes': incomes,
        'expenses': expenses,
    }
    return render(request, 'finanzas/dashboard.html', context)

@login_required
def investment_list(request):
    investments = Investment.objects.filter(user=request.user)
    return render(request, 'finanzas/investment_list.html', {'investments': investments})

@login_required
def saving_list(request):
    savings = Saving.objects.filter(user=request.user)
    return render(request, 'finanzas/saving_list.html', {'savings': savings})

@login_required
def income_list(request):
    incomes = Income.objects.filter(user=request.user)
    return render(request, 'finanzas/income_list.html', {'incomes': incomes})

@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'finanzas/expense_list.html', {'expenses': expenses})

# Vistas para Crear, Actualizar y Eliminar registros

# Inversiones
@login_required
def investment_create(request):
    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            investment = form.save(commit=False)
            investment.user = request.user
            investment.save()
            return redirect('dashboard')
    else:
        form = InvestmentForm()
    return render(request, 'finanzas/investment_form.html', {'form': form})

@login_required
def investment_update(request, pk):
    investment = get_object_or_404(Investment, pk=pk, user=request.user)
    if request.method == 'POST':
        form = InvestmentForm(request.POST, instance=investment)
        if form.is_valid():
            form.save()
            return redirect('investment_list')
    else:
        form = InvestmentForm(instance=investment)
    return render(request, 'finanzas/investment_form.html', {'form': form})

@login_required
def investment_delete(request, pk):
    investment = get_object_or_404(Investment, pk=pk, user=request.user)
    if request.method == 'POST':
        investment.delete()
        return redirect('investment_list')
    return render(request, 'finanzas/investment_confirm_delete.html', {'investment': investment})

# Repite procesos similares para Savings, Incomes y Expenses

def saving_create(request):
    # Lógica para crear un ahorro
    pass

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, f'Cuenta creada para {username}')
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'finanzas/signup.html', {'form': form})

def income_create(request):
    # Tu lógica para crear un ingreso
    pass

def expense_create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_de_gastos')  # Asegúrate de tener esta URL definida
    else:
        form = ExpenseForm()
    return render(request, 'finanzas/expense_form.html', {'form': form})
