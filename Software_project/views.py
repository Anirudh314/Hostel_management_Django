from django.shortcuts import render,redirect
def build_redirect(request):
    return redirect('/account/building')

def login_redirect(request):
    return redirect('/account/login')

def home(request):
    return render(request,'accounts/home_page.html')
