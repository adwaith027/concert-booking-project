from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required,user_passes_test
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND
from rest_framework import status,permissions
from django.contrib.auth import login,logout
from rest_framework.authtoken.models import Token
from rest_framework import status
# from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from .forms import userform,loginform,concertForm
from .models import usermodel,concertmodel,ticketbooking
from django.db.models import F 

def signup(request):
    if request.method=='POST':
        form=userform(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return HttpResponse('user created')
        else:
            return render(request,'signup.html',{'form':form})
    form=userform()
    return render(request,'signup.html',{'form':form})


@login_required(login_url='login')
def createconcert(request):
    if request.method=='POST':
        form=concertForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createconcert')
        else:
            return render(request,'concert.html',{'user':request.user,'form':form})
    form=concertForm()
    return render(request,'concert.html',{'user':request.user,'form':form})


@login_required(login_url='login')
def bookconcert(request):
    concert=concertmodel.objects.all()
    if request.method=='POST':
        ticketcount=request.POST.get('ticketsneeded')
        ticketcount=int(ticketcount)
        username=request.user.username
        useremail=request.user.email
        if ticketcount<=3 and ticketcount<=3:
            concert=request.POST.get('concertname')
            price=concertmodel.objects.filter(concertname=concert).values_list('ticketprice',flat=True)
            price=price[0]
            total=price*ticketcount
            ticketdata=ticketbooking(concertname=concert,ticketprice=price,username=username,useremail=useremail,bookedtickets=ticketcount,totalprice=total)
            ticketdata.save()
            concertmodel.objects
            return redirect('logout')
        else:
            return HttpResponse('no more than 3 tickets per user')
            # return render(request,'ticket.html',{'error':'One user can book only upto 3 tickets','concerts':concert})
    return render(request,'ticket.html',{'concerts':concert})


def userlogin(request):
    if request.method=='POST':
        form=loginform(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=usermodel.objects.get(username=username)
            if check_password(password,user.password):
                login(request,user) 
                if user.access=='admin':
                    return redirect('createconcert')
                else:
                    return redirect('bookconcert')
            else:
                return render (request,'login.html',{'form':form},{'error':'Invalid credentials'})
    form=loginform()
    return render (request,'login.html',{'form':form})

@login_required(login_url='login')
def userlogout(request):
    if request.method=='POST':
        logout(request)
        return redirect('login')
    return render(request,'logout.html',{'user':request.user})