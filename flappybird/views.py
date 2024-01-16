'''from django.shortcuts import render
def home(request):
 return render(request,'home.html',{'name':'Flappy bird'})
def download(request):
  #val1=int(request.POST['num1'])
 emailaddress = request.POST.get('emailaddress',null=False) 
 val2=int(request.POST['num2'],null=False)
 res=val2+emailaddress  
 return render(request,'result.html',{'result':res})
def dashboard(request):
 return render(request,'dashboard.html')
def flappybird(request):    
    return render(request,'result.html')'''
from django.shortcuts import render
from django.http import HttpResponseBadRequest
from .forms import *

def home(request):
    return render(request, 'home.html', {'name': 'Flappy bird'})

def flappybird(request):
    if request.method == 'POST':
        form = DownloadForm(request.POST)

        if form.is_valid():
            name=form.cleaned_data['name']
            emailaddress = form.cleaned_data['emailaddress']
            num2 = form.cleaned_data['num2']
            if len(str(num2))==10:
                res = num2
                return render(request,'result.html', {'result': res})
            else:
                return HttpResponseBadRequest("Invalid input. Please provide valid mobile number.")
        else:
            return HttpResponseBadRequest("Invalid input. Please provide valid data.")
    else:
        return render(request,'dashboard.html')

def dashboard(request):
    return render(request, 'dashboard.html')



