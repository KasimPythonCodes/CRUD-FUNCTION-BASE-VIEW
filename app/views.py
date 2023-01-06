from django.shortcuts import render
from app.forms import Studentform
# Create your views here.

def Registration(request):
    stu = Studentform(request.POST or None)
    if stu.is_valid():
        stu.save()
        stu =  Studentform()
    else:
        stu =  Studentform()
    return render(request , 'djangoform.html',{'stu':stu})       