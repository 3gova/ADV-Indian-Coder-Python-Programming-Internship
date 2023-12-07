from django.shortcuts import render,redirect,get_object_or_404
from taskapp.models import task
from taskapp.forms import taskform

# Create your views here.

def retriveview(request):
    tlist = task.objects.all()
    return render(request, 'taskapp/index.html',{'tlist':tlist})

def createview(request):
    forms = taskform()
    if request.method =='POST':
        forms = taskform(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/')
        
    return render(request, 'taskapp/create.html',{'form':forms})

def deleteview(request, id):
    tlist = task.objects.get(id=id)
    #tlist = get_object_or_404(task, id=id)
    tlist.delete()
    return redirect('/')

def updateview(request, id):
    tlist = task.objects.get(id=id)
    #tlist = get_object_or_404(task, id=id)
    if request.method =='POST':
        forms = taskform(request.POST,instance = tlist)
        if forms.is_valid():
            forms.save()
            return redirect('/')
               
    return render(request, 'taskapp/update.html',{'tlist':tlist})