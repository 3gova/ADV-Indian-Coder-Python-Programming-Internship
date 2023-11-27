from django.shortcuts import render
from .forms import calc

def calculator(request):
    result = 0
    
    if request.method == 'POST':
        form = calc(request.POST)

        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            operation = form.cleaned_data['operation']
            

            if operation == 'add':
                if (num1 or num2) == 0:
                    result = "0"
                else:
                    result = num1 + num2

            elif operation == 'sub':
                if num1 == num2:
                    result = "0"
                else:
                    result = num1 - num2

            elif operation == 'multi':
                if (num1 * num2) == 0:
                    result = "0"
                else:
                    result = num1 * num2

            elif operation == 'div':
                if num2 == 0:
                    result = "cannot divide by zero"
                elif num1 == 0:
                    result = "0"
                else:
                    result = num1 / num2

    else:
        form = calc()

    return render(request, 'calapp/index.html', {'form' : form , 'result' : result}) 