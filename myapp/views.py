from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from.forms import *

# Create your views here.
def signup(request):
    if request.method=='POST':
        form =NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username= username, password = password)
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form=NewUserForm()
        return render(request,'signup.html',{'form': form})

def loginpage(request):
    if request.method=='POST':
        usr=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(request,username=usr,password=pwd)

        if user is not None:
            login(request,user)
            return redirect('home')
        
        else:
            return HttpResponse("username and password not correct Try Again!")
            return render(request,'login.html')
    else:
            return render(request,'login.html')
    
def home(request):
        return render(request,'home.html', {'username': request.user.username.capitalize()})

def logoutpage(request):
        logout(request)
        return redirect('login')

def addemployee(request):
        if request.method=='POST':
            form =AddEmployeeForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('viewemployee')
        else:
            form=AddEmployeeForm()
            return render(request,"addemployee.html",{'form':form})

def viewemployee(request):
        employees=Employee.objects.all()
        return render (request,'viewemployee.html',{'employees':employees})

def deleteemployee(request,empid):
        data=Employee.objects.get(empid=empid)
        data.delete()
        employees=Employee.objects.all()
        return render(request,'viewemployee.html',{'employees':employees})

def editemployee(request,empid):
        data=Employee.objects.get(empid=empid)
        return render(request,'editemployee.html',{'data':data})

def updateemployee(request,empid):
        data=Employee.objects.get(empid=empid)
        form=AddEmployeeForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('viewemployee')
        else:
            return render(request,'editemployee.html',{'data':data})
        



            
     
            



