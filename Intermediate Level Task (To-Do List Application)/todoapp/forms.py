from django import forms
from todoapp.models import todo

# Create your models here.

class todo_form(forms.ModelForm):
    class Meta:
        model = todo
        fields = '__all__'
        
    

#data ---> information
#metadata----> data about data
#