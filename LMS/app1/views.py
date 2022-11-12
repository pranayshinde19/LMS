from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import BookModel
from app1.forms import registerform
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib import messages
from faker import Faker
import random,string
fake = Faker()
# Create your views here.


#to add data randomly using faler module
def run(request):
    for i in range(30):
        aname=fake.name()
        price_=fake.random_int(min=200,max=2500,step=50)
        bname=fake.bothify(text='???? ????????',letters=string.ascii_lowercase)
        type=random.choice(["non-fiction", "edited", "Reference","Fiction"])
        obj=BookModel.objects.create(book_name=bname,author_name=aname,price=price_,type_of_book=type)
        obj.save()
    return HttpResponse("<h1>DATA IS ADDED SUCCESSFULLY</h1>")

@login_required()
def home(request):
    datas=BookModel.objects.all()
    return render(request,'app1/home4.html',{'datas':datas})

def register(request):
    if request.method=='POST':
        data=registerform(request.POST)
        if data.is_valid():
            data.save()
            messages.success(request,' sucessfully done !!!')
            return redirect('/')
        else:
            messages.error(request,' ERROR , FILL CORRECT DETAILS !!!')
            return redirect('/register/')
    else :
        f=registerform()
        content={'form':f}
        return render(request,'app1/register.html', content)


@permission_required('app1.add_bookmodel' ,login_url="/errorshow/")
def add (request):
    if not request.user.is_authenticated:
        return redirect('/')
    elif request.method=='POST':
        if (request.method == 'POST'):
            bookname = request.POST['bookname']
            authorname = request.POST['authorname']
            price_= request.POST['price']
            booktype = request.POST['booktype']
            insert_data=BookModel.objects.create(book_name=bookname, author_name=authorname, price=price_, type_of_book=booktype)
            insert_data.save()
            return redirect('/')
    else :
        return render(request,'app1/add.html')

def errorshow(request):
    return render(request,'app1/errorshow.html')

@permission_required('app1.change_bookmodel' ,login_url="/errorshow/")
def update(request,tid):
    if not request.user.is_authenticated:
        return redirect('/')
    elif (request.method == 'POST'):
        bookname = request.POST['bookname']
        authorname = request.POST['authorname']
        price_= request.POST['price']
        booktype = request.POST['booktype']
        insert_data=BookModel.objects.filter(id=tid)
        insert_data.update(book_name=bookname, author_name=authorname, price=price_, type_of_book=booktype)
        return redirect('/')
    else:
        content={}
        content['data']=BookModel.objects.get(id=tid)
        return render(request,'app1/update.html',content)

@permission_required('app1.delete_bookmodel' ,login_url="/errorshow/")
def delete(request,tid):
    if not request.user.is_authenticated:
        return redirect('/')
    else :
        record_tobe_deleted = BookModel.objects.filter(id=tid)
        record_tobe_deleted.delete()
        return redirect('/')

def htol(request): #price
    if not request.user.is_authenticated:
        return redirect('/')
    datas=BookModel.objects.order_by('-price')
    data={"datas":datas}

    return render(request,'app1/home4.html',context=data)

def ltoh(request):#price
    if not request.user.is_authenticated:
        return redirect('/')
    datas=BookModel.objects.order_by('price')
    data={"datas":datas}
    return render(request,'app1/home4.html',context=data)

def AtoZ(request):#book
    if not request.user.is_authenticated:
        return redirect('/')
    datas=BookModel.objects.order_by('book_name')
    data={"datas":datas}
    return render(request,'app1/home4.html',context=data)

def ZtoA(request):#book
    if not request.user.is_authenticated:
        return redirect('/')
    datas=BookModel.objects.order_by('-book_name')
    data={"datas":datas}
    return render(request,'app1/home4.html',context=data)

def AatoZz(request):#author
    if not request.user.is_authenticated:
        return redirect('/')
    datas=BookModel.objects.order_by('author_name')
    data={"datas":datas}
    return render(request,'app1/home4.html',context=data)

def ZztoAa(request):#author
    if not request.user.is_authenticated:
        return redirect('/')
    datas=BookModel.objects.order_by('-author_name')
    data={"datas":datas}
    return render(request,'app1/home4.html',context=data)

def lowtohigh(request):#id
    if not request.user.is_authenticated:
        return redirect('/')
    datas=BookModel.objects.order_by('id')
    data={"datas":datas}
    return render(request,'app1/home4.html',context=data)

def hightolow(request):#id
    if not request.user.is_authenticated:
        return redirect('/')
    datas=BookModel.objects.order_by('-id')
    data={"datas":datas}
    return render(request,'app1/home4.html',context=data)

def CAtoZ(request):#category
    if not request.user.is_authenticated:
        return redirect('/')
    datas=BookModel.objects.order_by('type_of_book')
    data={"datas":datas}
    return render(request,'app1/home4.html',context=data)

def CZtoA(request):#category
    if not request.user.is_authenticated:
        return redirect('/')
    datas=BookModel.objects.order_by('-type_of_book')
    data={"datas":datas}
    return render(request,'app1/home4.html',context=data)

def catfilter(request,cat):#filter category
    if not request.user.is_authenticated:
        return redirect('/')
    content={}
    content['datas']=BookModel.objects.filter(type_of_book=cat)
    return render(request,'app1/home4.html',content)
