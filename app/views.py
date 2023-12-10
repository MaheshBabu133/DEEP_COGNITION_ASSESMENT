from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from app.models import *
from app.forms import *
from django.urls import reverse

from app.serializers import *
from rest_framework import viewsets
from app.serializers import *
from rest_framework.response import Response

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required


def Registration(request):
    d = {'UMF':UserMOdelForm()}
    if request.method == "POST":
        UMF = UserMOdelForm(request.POST)
        if UMF.is_valid():
            NUMF = UMF.save(commit = False)
            password = UMF.cleaned_data['password']
            NUMF.set_password(password)
            NUMF.save()
            return HttpResponse("Registration done Succefully")
        else:
            return HttpResponse("Invalid Data")

    return render(request,'Registration.html',d)



def Home(request):
    if request.session.get('username'):
        username = request.session.get('username')
        d = {'username' : username}
        return render(request,'Home.html',d)




    return render(request,'Home.html')
from faker import Faker
ob = Faker()


def InsertData(request):
    d = {'EMP':EMP()}
    if request.method == 'POST' and request.FILES:
        
        EMP_data = EMP(request.POST,request.FILES)
        if EMP_data.is_valid():
            NEMP_data = EMP_data.save(commit = False)
            NEMP_data.identity = 'AADCE' + ob.zipcode()
            NEMP_data.save()
            return HttpResponse("Data save Succsfully")
               
    return render(request,'InsertData.html',d)



#Super User Login username,password = anusha,anusha

def user_login(request):
    if request.method=="POST":
        username=request.POST['un']
        password=request.POST['pw']
        print(username,password)
        AUO=authenticate(username=username,password=password)
        print(AUO)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('Home'))
        else:
            return HttpResponse('invalid username or password')
        
    return render(request,'user_login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Home'))

@login_required
def change_password(request):
    if request.method=='POST':
        pw=request.POST['pw']
        username=request.session.get('username')
        UO=User.objects.get(username=username)
        UO.set_password(pw)
        UO.save()
        return HttpResponse('change_password is successfull')
    return render(request,'change_password.html')


def forget_password(request):
    if request.method=='POST':
        username=request.POST['username']
        pw=request.POST['pw']
        LUO=User.objects.filter(username=username)
        if LUO:
            UO=LUO[0]
            UO.set_password(pw)
            UO.save()
            return HttpResponse('<h1>Password change successfully</h1>')
        else:
            return HttpResponse("user not found")
    return render(request,'forget_password.html')
    

class EMPDATA(viewsets.ViewSet):
    def list(self,request):
        SPO = employee_data.objects.all()
        SED = EMPMS(SPO,many = True)
        username = request.session.get('username')
        print(username)
        d = {'data' : SED.data,'username':username,'EMP':SPO}
        return render(request,'list.html',d)
    def retrieve(self,request,pk):
        TO=employee_data.objects.get(pk=pk)
        SDO=EMPMS(TO)
        return Response(SDO.data)

    def update(self,request,pk):
        SPO=employee_data.objects.get(pk=pk)
        SPD=EMPMS(SPO,data=request.data)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'Fredom fighters is updated'})
        else:
            return Response({'Failed':'Fredom fighters is Not Updated'})
    
    def partial_update(self,request,pk):
        SPO=employee_data.objects.get(pk=pk)
        SPD=EMPMS(SPO,data=request.data,partial=True)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'Fredom fighters is updated'})
        else:
            return Response({'Failed':'Fredom fighters is Not Updated'})
    def destroy(self,request,pk):
        employee_data.objects.get(pk=pk).delete()
        return Response({'Deleted':'Fredom fighters data is deleted'})


