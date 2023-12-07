from django.contrib import admin
from taskapp.models import task

# Register your models here.

class taskadmin(admin.ModelAdmin):
    list = ['sno','task_name','status']
admin.site.register(task,taskadmin)