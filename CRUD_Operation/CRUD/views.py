from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.contrib import messages

# Insert Operation

def index(request):
    if request.method == 'POST':
        form  = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.info(request,'insert successfuly..')
                return redirect('index')
            except: 
                pass
    else:
        form = EmployeeForm
        args = {'form':form}
        return render(request,'Index.html',args)

# Showe Data Operation

def show(request):
    employees = Employee.objects.all()
    return render(request,'show.html',{'employees':employees})

# Edit Operation

def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,'edit.html',{'employee':employee})

def update(request, id):
    employee = Employee.objects.get(id=id)
    form  = EmployeeForm(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return render(request,'show.html')
    return render(request,'edit.html',{'employee':employee})

# Delete Operation

def delete(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('show')