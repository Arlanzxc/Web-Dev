from django.contrib import admin
from .models import Company, Vacancy
# Register your models here.
# api/admin.py

admin.site.register(Company)
admin.site.register(Vacancy)