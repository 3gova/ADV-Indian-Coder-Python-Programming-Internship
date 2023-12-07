from django import forms
from taskapp.models import task

# Create your models here.

class taskform(forms.ModelForm):
    class Meta:
        model = task
        fields = '__all__'
        
    

#data ---> information
#metadata----> data about data
#