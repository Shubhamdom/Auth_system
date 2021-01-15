from django.shortcuts import render,redirect
from .models import userInfo,item
from django.contrib import messages
from django.contrib.auth.models import User, auth
#from .forms import category,subcategory

# Create your views here.

def home(request):
    items = item.objects.all()
    context = {'items': items}
    return render(request,'home.html',context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST['pwd']
        user = auth.authenticate(request,username=username,password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('dash')

        if user is None:
            messages.add_message(request, messages.ERROR, "invalid credentials")
            return redirect('login')

    return render(request,'login.html')



def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST.get('email',False)
        contact = request.POST['contact_no']
        password = request.POST['pwd']

        #User.objects.create_user(username=email,password=password).save()
        userInfo(name=name,email=email,phone=contact,password=password).save()
        User.objects.create_user(username=email, email=email,password=password).save()
        messages.add_message(request, messages.ERROR, "Registration successful")

        return render(request,'login.html')



    return render(request,'registration.html')


def dash(request):
    items_count = item.objects.filter(username=request.user.username).count()
    items = item.objects.filter(username=request.user.username)
    context = {'items': items,'count':items_count}

    return render(request, 'dash.html',context)
    messages.add_message(request, messages.ERROR, "logout successful")
    return redirect(request.META['HTTP_REFERER'])




def logut(request):
    auth.logout(request)
    return redirect('login')
    return redirect(request.META['HTTP_REFERER'])

def additem(request):
    if request.method=='POST':
        name = request.POST['name']
        price = request.POST['price']
        category=request.POST['category']
        subcategory=request.POST['activity']
        qut = request.POST['qut']

        username = request.user.username
        item(username=username,name=name,prce=price,category=category,subcategory=subcategory,description=qut).save()
        return redirect('dash')
    return render(request,'item.html')


def deleteitem(request,itemid):
    item.objects.filter(id=itemid).delete()
    return redirect('dash')




def updateitem(request,itemid):

    if request.method=='POST':
        name = request.POST.get('name',False)
        price = request.POST.get('price',False)
        category = request.POST.get('category',False)
        description = request.POST.get('qut',False)

        item.objects.filter(id=itemid).update(name=name,prce=price,category=category,description=description)
        return redirect('dash')

    data = item.objects.filter(id=itemid)
    context = {'data': data}
    return render(request,'updateitem.html',context)



def viewmore(request,itemid,category):
    data = item.objects.filter(id=itemid)
    cate = item.objects.filter(category=category)
    context={
        'data':data,
        'cate':cate
    }
    return render(request,'viewmore.html',context)

def viewmoreseller(request,itemid):
    data = item.objects.filter(id=itemid)
    context={
        'data':data
    }
    return render(request,'viewmoreseller.html',context)


#admin login
def adminlogin(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['pwd']
        if uname=='shubhamdom19@gmail.com' and pwd=='9970273727':
            return redirect('admindash')
    return render(request,'adminlogin.html')

def admindash(request):
    return render(request,'admindash.html')
'''def addcategory(request):

    if request.method == 'POST':
        form = category(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'admindash.html')
    form = ()

    return render(request,'admindash.html',{
        'form':form
    })'''