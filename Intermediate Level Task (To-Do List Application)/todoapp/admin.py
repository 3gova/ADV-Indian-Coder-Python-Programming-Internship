from django.contrib import admin
from todoapp.models import todo

# Register your models here.

class todoadmin(admin.ModelAdmin):
    list = ['sno','task_name','status']
admin.site.register(todo,todoadmin)