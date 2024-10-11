from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Investment, Saving, Income, Expense

admin.site.register(Investment)
admin.site.register(Saving)
admin.site.register(Income)
admin.site.register(Expense)
