from django.shortcuts import render
from app.models import Employee



# Create your views here.
def read_data(request):
    Employee_list=Employee.objects.all()
    context={
        "Employee_list":Employee_list
    }

    return render(request,"read.html",context)

def read_one_data(request,id):#id=5
    Employee=Employee.objects.get(id=id)
    context={
        'Employee':Employee
    }
    return render(request,"readone.html",context)
    

