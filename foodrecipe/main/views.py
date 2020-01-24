from django.shortcuts import render, redirect
from django.http import HttpResponse,request
from .forms import RegistrationForm
from  django.contrib.auth.models import User, auth
from  django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm



def home(request):
    user=request.user
    return render(request,'main/index.html',{'user':user})


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
           form.save()
           email = form.cleaned_data.get('email')
           password = form.cleaned_data.get('password1')
           user = authenticate(email = email, password = password)
           login(request, user)
           return redirect('Homepage')

    else:
        form = RegistrationForm()
    return render(request ,'main/register.html', {'form': form})   
    #        return redirect('home')
    #     else:
    #          return redirect('register')
    # else:
    #     form = RegistrationForm
    #     context['form'] = form
    # return render(request,'main/register.html',context)


def Login(request):
    print("sdfsdfsdf")
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            print("sdfasdfasdfsdf")
            username = form.cleaned_data.get("username")
            print("username",username)
            password = form.cleaned_data.get("password")
            user = auth.authenticate(username = username, password = password)
            print('user is ',user)
            if user is not None:
                auth.login(request, user)
                # messages.success(request, f'you have logged as {{ username }}')
                return redirect('Homepage')
 
    form = AuthenticationForm()
    return render(request, "main/login.html", context = {"form" : form})	
   

def Logout(request):
    logout(request)
    return redirect('Homepage') 
   
   
   
#     # context ={}
#     # if request.method == 'POST':
#     #     form = AuthenticationForm(request, data = request.POST)
#     #     username=request.POST['username']
#     #     password = request.POST['password']
#     #     print("sadfasdfasdf",username)
#     #     user= auth.authenticate(username=username,password=password)
#     #     if user is not None:
#     #        auth.login(request,user)
#     #        print("login successfull")
#     #        return redirect('register')
        
#     #     else:
#     #         context["error"]="invalid password and username"
#     #         return render(request,'main/login.html',context)
#     # else:
#     #     return render(request,'main/login.html',context)
    
