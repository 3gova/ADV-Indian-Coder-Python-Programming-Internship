from django import forms

OPERATION_CHOICES = [
    ('add', 'Addition'),
    ('sub', 'Subtraction'),
    ('multi', 'Multipilcation'),
    ('div','Division'),
]

class calc(forms.Form):
    num1 = forms.FloatField(label = 'Number 1', required=True)
    num2 = forms.FloatField(label = 'Number 2', required=True)
    #operation = forms.ChoiceField(choices = OPERATION_CHOICES, label='Operation')
    operation = forms.ChoiceField( label="Select Operation",
                        widget=forms.RadioSelect,choices=OPERATION_CHOICES)
   