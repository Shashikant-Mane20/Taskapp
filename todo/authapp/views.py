from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def user_register(request):
    if request.method =='POST':
        #Fetching Data
        uname=request.POST['uname']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']
        uemail=request.POST['uemail']

        print("Method Type:",request.method)
        print("Username:",uname)
        print("Password:",upass)
        print("Confirm Password:",ucpass)
        print("email:",uemail)

        #validation of data
        context={}
        if uname=="" or upass=="" or ucpass=="" or uemail=="":
            context['errmsg']="Field cannot be Blank"
            return render(request,"authapp/register.html",context)
        elif upass!=ucpass:
            context['errmsg']="Password and Confirm Password Mismatch"
            return render(request,"authapp/register.html",context)
        else:
            # u=User.objects.create(username=uname,password=upass,email=uemail)
            u=User.objects.create(username=uname,email=uemail)
            u.set_password(upass) # to store password in encrypted format in database
            u.save()
            context['success']="Account Created Successfully!! Please Login"

            # return HttpResponse("User Created Successfully")
            # return redirect('/authapp/login')
            return render(request,"authapp/register.html",context)
    else:
        print("Method Type:",request.method)
        return render(request,'authapp/register.html')
    

def user_login(request):
    if request.method =='POST':
        #Fetching Data
        uname=request.POST['uname']
        upass=request.POST['upass']

        print('Method Type:',request.method)
        print('Username:',uname)
        print('Password:',upass)

        u=authenticate(username=uname,password=upass)
        # print("User Object:",u)
        # print("ID:",u.id)
        # print("Username:",u.username)
        # print("Password",u.password)
        # print("Email:",u.email)
        # print("SuperUser:",u.is_superuser)

        if u is not None:
            login(request,u)
            return redirect('/home')
        else:
            context={}
            context['errmsg']="Invalid Username and Password"
            return render(request,'authapp/login.html',context)
            # return HttpResponse("Invalid Username and Password")
        
        # return HttpResponse("Details Fetched")
    else:
         print('Method Type:',request.method)
         return render(request,'authapp/login.html')
        # return HttpResponse("User login successfully")
      

def user_logout(request):
    logout(request) #destroy data of the logged in user from session.
    return redirect('/authapp/login')