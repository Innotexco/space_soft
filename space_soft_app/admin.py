from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Contact)
# admin.site.register(Course_Intrest)
# admin.site.register(Student)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "contact", "address","message")
    list_filter = ["name"]
    ordering = ["name"] # sort name alphabetical order
    search_fields = ['name', 'email']

@admin.register(Course_Intrest)
class Course_IntrestAdmin(admin.ModelAdmin):
    list_display = ("name", "course", "message")
    list_filter = ["course"]
    ordering = ["course","name"] # sort name alphabetical order
    search_fields = ['name', 'course']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("full_name", "gender", "phone_number","residential_address", "marital_status", "course", "class_mode", "reason")
    list_filter = ["course", "class_mode", "marital_status"]
    ordering = ["full_name","course", "class_mode"] # sort name alphabetical order
    search_fields = ['full_name', 'course', 'class_mode']