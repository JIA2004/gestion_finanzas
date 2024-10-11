from django import forms
from .models import Investment, Saving, Income, Expense
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = ['ticker', 'company_name', 'quantity', 'purchase_price', 'purchase_date']
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
        }

class SavingForm(forms.ModelForm):
    class Meta:
        model = Saving
        fields = ['name', 'amount', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['source', 'amount', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Requerido. Ingrese un email válido.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

