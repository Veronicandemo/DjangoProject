from django.contrib import admin

# Register your models here.
from .models import Employee,Student

# Register your models here.
class EmployeeAdmin (admin.ModelAdmin):
    list_display = ("first_name", "last_name","age","country","phone_number","residence_area","role","email","gender")
    search_fields  = ("first_name", "last_name",)
admin.site.register(Employee,EmployeeAdmin)  


class StudentAdmin (admin.ModelAdmin):
    list_display = ("first_name", "last_name","age","residential_area","lab","countries")
    search_fields  = ("first_name", "last_name",)
admin.site.register(Student,StudentAdmin)