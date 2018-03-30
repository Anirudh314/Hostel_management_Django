from django.shortcuts import render, HttpResponse, redirect
from accounts.forms import room_form1
from django.contrib.auth.models import User
from accounts.models import room_form
from django.shortcuts import render
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm

# Create your views here.
def home(request):
    return render(request , 'accounts/home.html')

def building(request):
    return render(request, 'accounts/buildings.html')      

def floormapLG(request):
    return render(request, 'accounts/floormapLG.html')    

def floormapL1(request):
    return render(request, 'accounts/floormapL1.html')    

def floormapL2(request):
    return render(request, 'accounts/floormapL2.html')   

def floormapMG(request):
    return render(request, 'accounts/floormapMG.html')    

def floormapM1(request):
    return render(request, 'accounts/floormapM1.html')    

def roomform(request):
    return render(request, 'accounts/room_form.html')

def home_page(request):
    return render(request,'accounts/home_page.html')


def profile(request):
    return render(request,'accounts/profile.html')


def home_page_booked(request):
    return render(request,'accounts/home_page_booked.html')


def login(request):
	return render(request,'account/login.html')

def logout(request):
	return render(request,'account/home.html')


def register1(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            password =  userObj['password1']
            email =  userObj['email']
        
          #  password2 =  userObj['password2']
           # usn   =   userObj['usn']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                try:
                    User.objects.create_user(username,  email,password)
                    user = authenticate(username = username, password = password)
                    #login(request) #login(request, user)
                    return HttpResponseRedirect('/account/home_page')
                
                except Exception as e:
                    if(type(e) == "TypeError"):
                        #form = UserRegistrationForm()
                        #return render(request, 'accounts/register_corr.html', {'form' : form})
                        return HttpResponseRedirect('/account/home_page')
    
            else:
                #raise forms.ValidationError('Looks like a username with that email or password already exists')
                form = UserRegistrationForm()
                return render(request, 'accounts/register_wr.html', {'form' : form})
    else:
        form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'form' : form})  


    form = UserRegistrationForm()
    return render(request, 'accounts/register_corr.html', {'form' : form})   


def register2(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            password =  userObj['password1']
            email =  userObj['email']
        
          #  password2 =  userObj['password2']
           # usn   =   userObj['usn']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                try:
                    User.objects.create_user(username,  email,password)
                    user = authenticate(username = username, password = password)
                    #login(request) #login(request, user)
                    return HttpResponseRedirect('/account/home_page')
                
                except Exception as e:
                    if(type(e) == "TypeError"):
                        #form = UserRegistrationForm()
                        #return render(request, 'accounts/register_corr.html', {'form' : form})
                        return HttpResponseRedirect('/account/home_page')
    
            else:
                #raise forms.ValidationError('Looks like a username with that email or password already exists')
                form = UserRegistrationForm()
                return render(request, 'accounts/register_wr.html', {'form' : form})
    else:
        form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'form' : form})  


    form = UserRegistrationForm()
    return render(request, 'accounts/register_corr.html', {'form' : form})   


def register3(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            password =  userObj['password1']
            email =  userObj['email']
        
          #  password2 =  userObj['password2']
           # usn   =   userObj['usn']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                try:
                    User.objects.create_user(username,  email,password)
                    user = authenticate(username = username, password = password)
                    #login(request) #login(request, user)
                    return HttpResponseRedirect('/account/home_page')
                
                except Exception as e:
                    if(type(e) == "TypeError"):
                        #form = UserRegistrationForm()
                        #return render(request, 'accounts/register_corr.html', {'form' : form})
                        return HttpResponseRedirect('/account/home_page')
    
            else:
                #raise forms.ValidationError('Looks like a username with that email or password already exists')
                form = UserRegistrationForm()
                return render(request, 'accounts/register_wr.html', {'form' : form})
    else:
        form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'form' : form})  

    form = UserRegistrationForm()
    return render(request, 'accounts/register_corr.html', {'form' : form})   





#New function for room booking
def book_room(request):
    if(request.method == 'POST'):
        form = room_form1(request.POST)
        if form.is_valid():    
            obj = form.cleaned_data
            username = obj['usn']
            room = obj['room_no']
            if not room_form.objects.filter(usn=username).exists() and len(room_form.objects.filter(room_no=room)) < 3:
                form.save()
                return redirect('/account/home_page_booked')
            elif room_form.objects.filter(usn=username).exists():
                form = room_form1
                args = {'form': form}
                return render(request, 'accounts/room_form_exs.html', args)
            else:
                form = room_form1
                args = {'form': form}
                return render(request, 'accounts/room_form_exs2.html', args)
        else:
            form = room_form1
            args = {'form': form}
            return render(request, 'accounts/room_form_wr.html', args)   
    else:
        form = room_form1
        args = {'form': form}
        return render(request, 'accounts/room_form.html', args)


