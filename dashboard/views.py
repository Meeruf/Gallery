from django.shortcuts import render, HttpResponse

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login/')
def dashboard(request):


    return render(request, 'dashboard/dashboard.html', context={})
    
    


def login_dashboard(request):
    return render(request, 'dashboard/login.html', context={})