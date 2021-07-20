from django.shortcuts import render
from .models import Student

# Create your views here.
def view1(request):
    s=Student.objects.all()
    d={'stud':s}
    return render(request,'myApp/one.html',d)
