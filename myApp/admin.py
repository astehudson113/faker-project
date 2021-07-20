from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    L=['name','roll','marks','dob','email']

admin.site.register(Student,StudentAdmin)    
