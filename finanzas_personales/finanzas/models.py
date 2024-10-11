from django.db import models
from django.contrib.auth.models import User

class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticker = models.CharField(max_length=10)
    company_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()
    precio_actual = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.company_name} ({self.ticker})"
    
    @property
    def valor_actual(self):
        if self.precio_actual:
            return self.precio_actual * self.quantity
        return None

    @property
    def ganancia(self):
        if self.valor_actual:
            return self.valor_actual - (self.purchase_price * self.quantity)
        return None

    @property
    def precio_actual_display(self):
        return f"${self.precio_actual:.2f}" if self.precio_actual else 'N/A'
    
    @property
    def valor_actual_display(self):
        return f"${self.valor_actual:.2f}" if self.valor_actual else 'N/A'
    
    @property
    def ganancia_display(self):
        return f"${self.ganancia:.2f}" if self.ganancia is not None else 'N/A'

class Saving(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.name

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.source} - {self.amount}"

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.category} - {self.amount}"
