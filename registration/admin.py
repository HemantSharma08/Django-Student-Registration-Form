from django.contrib import admin

# Register your models here.
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','firstname','lastname','date','email','mobile','gender','address','city','pincode','state','country')