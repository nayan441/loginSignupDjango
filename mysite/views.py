
from django.shortcuts import redirect, render
from django.http import HttpResponse
from  django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

# Create your views here.

def index(request):
    return render(request,'index.html')
    # return HttpResponse('''<H1 style="text-align:center; color:blue;"> Hello world</H1''')

def signup(request):
    if request.method == "POST":
        username=request.POST.get("username")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")

        new_user = User.objects.create_user(username,email,password1)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()
        messages.success(request,"user successfully created")
        return render(request, 'index.html')
    return render(request,'signup.html')
def signin(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        print("\n\n")
        print(username)
        print(password1)
        user = authenticate(username = username, password = password1)
        print(password1)
        if user is not None:
            login(request,user)
            firstname=user.first_name
            lastname= user.last_name
            messages.success(request,"Successfully login")
            return render(request,'index.html',{'firstname':firstname,'lastname':lastname})
        else:
            messages.error(request,"bad cardinalities")
            return render(request,'signin.html')
    return render(request, 'signin.html')
def signout(request):
    logout(request)
    # messages.error(request,"logout successfully")
    return render(request,'signout.html')