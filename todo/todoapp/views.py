from django.shortcuts import render,HttpResponse,redirect
from todoapp.models import TaskList
from django.db.models import Q
# Create your views here.
def dashboard_page(request):

    # return HttpResponse("Hello From Contact Page!!!")
    # return redirect('/home')
    return render(request,'todoapp/dashboard.html')

def home_page(request):
    # print(request.user)
    # print(request.user.id)
    # print(request.user.username)
    # print(request.user.is_superuser)
    # print('Value:',request.user.is_authenticated)
    if request.user.is_authenticated:
        q1=Q(is_activate=1)
        q2=Q(user_id=request.user.id)
        # t=TaskList.objects.filter(is_activate=1)
        t=TaskList.objects.filter(q1 & q2)
    # print(t)
    # for x in t:
    #     print("ID:",x.id)
    #     print("Title:",x.title)
    #     print("Details:",x.detail)
    #     print("Due Date:",x.due_dt)
    #     print("Is Completed:",x.is_completed)
    #     print("Is activate:",x.is_activate)
    #     print()
    # return HttpResponse("<h1>Hello From Home Page!!!</h1>")

        context={}
        context['data']=t
        return render(request,'todoapp/dashboard.html',context)
    else:
        return redirect('/authapp/login')


def about_page(request):

    return HttpResponse("Hello From about Page!!!")

def product_page(request):

    return HttpResponse("Hello From Product Page!!!")


def add_task(request):

    # return HttpResponse("In Add task section")
    print("Method Type:",request.method)

    if request.method=="POST":#GET==POST False| POST==POST=> True
        # print("In if section")
        # return HttpResponse("Insert data into database")
        #fetch form data
        t=request.POST['title']
        d=request.POST['det']
        dt=request.POST['duedt']
        print('Title:',t)
        print("Details:",d)
        print("Date:",dt)
        t=TaskList.objects.create(title=t,detail=d,due_dt=dt,user_id=request.user)
        t.save()
        return redirect('/home')
        # return HttpResponse("Data inserted succesfully into database table")
    
        # return HttpResponse("Data fetch from the form")

    else:
        print("In else section")
        return render(request,'todoapp/addtask.html')
    
def dtl(request):
    context={}
    context['a']=2000
    context['b']=50
    context['User']='Shashikant'
    context['l']=[10,20,30,40,50,60]
    return render(request,'todoapp/dashboard.html',context)

def delete_task(request,rid):
    # print("ID to be deleted:",rid)
    # return HttpResponse("ID to be deleted:"+rid)
    #t=TaskList.objects.get(id=rid) #select * from tablename where id=3
    # print(t)
    # t.delete()
    # return HttpResponse('record Fetched')
    # return HttpResponse("Object Deleted")
    t=TaskList.objects.filter(id=rid)
    t.update(is_activate=0)
    return redirect('/home')

def edit_task(request,rid):
    # print("ID to be edited:",rid)
    # return HttpResponse("ID to be edited"+rid)

    if request.method =="POST":
        ut=request.POST['title']
        ud=request.POST['det']
        udt=request.POST['duedt']
        print("Updates Title:",ut)
        print("Updated Details:",ud)
        print("Updated Date:",udt)
        t=TaskList.objects.filter(id=rid)
        t.update(title=ut,detail=ud,due_dt=udt)
        return redirect("/home")
        return HttpResponse("Details Fetched")
    else:
        t=TaskList.objects.get(id=rid)
        context={}
        context['data']=t
        return render(request,'todoapp/editform.html',context)
    
def mark_completed(request,rid):
    t=TaskList.objects.filter(id=rid)
    t.update(is_completed=1)
    
    return redirect('/home')
