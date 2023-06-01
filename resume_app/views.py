from django.http import HttpResponseRedirect
from django.shortcuts import render

from resume_app.models import Create
from .forms import CreateForm, LoginForm,Register
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group


# Create your views here.
def home(request):
  return render(request,"home.html")

# signup
def register(request):
 if not request.user.is_authenticated:
    if request.method=="POST":
        fm=Register(request.POST)
        if fm.is_valid():
            user=fm.save()
            group=Group.objects.get(name="others")
            user.groups.add(group)
        return HttpResponseRedirect('/login/')
    else:
        fm=Register()
    return render (request,"register.html",{"form":fm})
 else:
  return HttpResponseRedirect('/Create/')


def Create1(request):
 if request.user.is_authenticated:  
     if request.method=="POST":
        fm=CreateForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            print(fm)
            return HttpResponseRedirect('/details/')
     else:
        fm=CreateForm()
     return render (request,"Create.html",{"form":fm})
 else:
  return HttpResponseRedirect('/login/')

def details(request):
    if request.user.is_authenticated:
       info=Create.objects.all ()
       return render (request,"details.html",{"info":info})
    else:
     return HttpResponseRedirect('/login /')


def user_login(request):
 if not request.user.is_authenticated:
    if request.method=="POST":
        fm = LoginForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
            return HttpResponseRedirect('/Create/')
    else:
        fm=LoginForm()
    return render (request,"login.html",{"form":fm})
 else:
  return HttpResponseRedirect('/Create/')

    
def user_logout(request):
    logout(request)
    print("hi")
    return HttpResponseRedirect('/')



def candidate(request,id):
 if request.user.is_authenticated:
    fm=Create.objects.get(pk=id)
    print(fm)
    return render(request,"candidate.html",{"fm":fm})
 else:
  return HttpResponseRedirect('/login/')


# 
def Update(request,id):
 if request.user.is_authenticated:
    if request.method=="POST":
        pi=Create.objects.get(pk=id)
        form=CreateForm(request.POST,instance=pi)
        if form.is_valid():
                form.save()
        return HttpResponseRedirect('/details/')
    else:
        pi=Create.objects.get(pk=id)
        form=CreateForm(instance=pi)
    return render (request,"Update.html",{"form":form})
 else:
  return HttpResponseRedirect('/login/')


def Delete_resume(request,id):
 if request.user.is_authenticated:
    if request.method=="POST":
        pi=Create.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/details/')
 else:
  return HttpResponseRedirect('/login/')
  


