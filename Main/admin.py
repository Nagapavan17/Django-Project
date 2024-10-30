from django.contrib import admin
from .models import Employee
# Register your models here.
class EmpInfo(admin.ModelAdmin):
    list_display=['username','email']

admin.site.register(Employee,EmpInfo)