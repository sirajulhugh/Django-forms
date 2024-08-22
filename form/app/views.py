from django.shortcuts import render,redirect
from app.models import Employee
from app.forms import Employeeforms

# Create your views here.
def add(request):
    form=Employeeforms()
    return render(request,"add.html",{'forms':form})

def addemp(request):
    if request.method=='POST':
        form=Employeeforms(request.POST)
        if form.is_valid:
            form.save()
            return redirect('show')
        return render(request,'add.html')
    
def show(request):
    emp=Employee.objects.all()
    return render(request,'show.html' ,{'emp':emp})

def update(request,id):
    std=Employee.objects.get(id=id)
    form=Employeeforms(instance=std)
    if request.method=='POST':
        form=Employeeforms(request.POST,instance=std)
        if form.is_valid:
            form.save()
            return redirect('show')
    else:
        return render(request,"update.html",{'form':form})
    
def delete(request,id):
    std=Employee.objects.get(id=id)
    # form=Employeeforms(instance=std)
    std.delete()
    # form.save()
    return redirect('show')
    
    
