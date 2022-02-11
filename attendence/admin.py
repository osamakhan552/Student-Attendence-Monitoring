from django.contrib import admin
from .models import Student,Product


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'pname', 'pnumber', 'price']
# Register your models here.
