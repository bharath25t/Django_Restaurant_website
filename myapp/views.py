from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

from .forms import *
def about(request):
    return render(request,"about.html")
def home(request):
    return render(request,"home.html")
def service(request):
    return render(request,"service.html")
def contact(request):
    return render(request,"contact.html")
def disp_form(request):
    o=student_form()
    return render(request,'forms.html',{'f':o})