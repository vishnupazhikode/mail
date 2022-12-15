from email import message
from django.shortcuts import render,redirect
from siteadmin.models import *
from user.models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def loginAction(request):
   username=request.POST['username']
   password=request.POST['password']
   admin=admin_tb.objects.filter(username=username,password=password)
   user=register_tb.objects.filter(username=username,password=password)
   if admin.count()>0:
        request.session['id']=admin[0].id
        return render(request,'home.html')
   elif user.count()>0:
        request.session['id']=user[0].id
        return render(request,"userhome.html")

   else:
        return redirect('login')

def addhobby(request):
    return render(request,'addhobby.html')

def addhobbyAction(request):
    hobbyname=request.POST["hobbyname"]
    hobby=hobbyname_tb(name=hobbyname)
    hobby.save()
    messages.add_message(request,messages.INFO,"added successfully hobby")
    return redirect('addhobby')

def factor(request):
    hobby=hobbyname_tb.objects.all()
    return render(request,'factor.html',{'factor':hobby})
def factorAction(request):
    hobby=request.POST['hobbyname']
    factorname=request.POST['factorname']
    user=hobbyfactor_tb(hobbyid_id=hobby,factorname=factorname)
    user.save()
    messages.add_message(request,messages.INFO,'submitted sucessfully')
    return redirect('factor')

def season(request):
    return render(request,"season.html")
def seasonAction(request):
    season=request.POST['seasonname']
    user=season_tb(seasonname=season)
    user.save()
    messages.add_message(request,messages.INFO,'added sucessfully')
    return redirect('season')

def seasonfactor(request):
    season=season_tb.objects.all()
    return render(request,'seasonfactor.html',{'sf':season})
def seasonfactorAction(request):
    season=request.POST['seasonname']
    factors=request.POST['factorname']
    user=seasonfactor_tb(seasonid_id=season,factor=factors)
    user.save()
    messages.add_message(request,messages.INFO,'added to table')
    return redirect('seasonfactor')

def seasoncountry(request):
    season=season_tb.objects.all()
    country=country_tb.objects.all()
    return render(request,'seasoncountry.html',{'sea':season,'count':country})
def getfactor(request):
    sid=request.GET['season_id']
    factor=seasonfactor_tb.objects.filter(seasonid=sid)
    return render(request,'getfactor.html',{'factor':factor})

def seasoncountryAction(request):
    seasonname=request.POST['season']
    factor=request.POST['factor']
    counn=request.POST['country']
    state=request.POST['state']
    month=request.POST['month']
    user=seasoncountry_table(seasonid_id=seasonname,factorid_id=factor,countryid_id=counn,stateid_id=state,months=month)
    user.save()
    messages.add_message(request,messages.INFO,"added to table")
    return redirect("seasoncountry")

def agefactor(request):
    return render(request,'agefactor.html')

def agefactorAction(request):
    minage=request.POST['minage']
    maxage=request.POST['maxage']
    factorname=request.POST['factor']
    user=agefactor_tb(minage=minage,maxage=maxage,factor=factorname)
    user.save()
    messages.add_message(request,messages.INFO,'success')
    return redirect('agefactor')
     
def forgotpassword(request):
    return render(request,'forgotpassword.html')
def forgotpasswordAction(request):
    los=request.POST['username']
    user=register_tb.objects.filter(username=los)
    counts=country_tb.objects.all()
    if user.count()>0:
        return render(request,'newpassword.html',{'country':counts})
    else:
        messages.add_message(request,messages.INFO,'INCORRECT USERNAME')
    return redirect('forgotpassword')

def newpasswordAction(request):
    name=request.POST['name']
    dob=request.POST['dob']
    country=request.POST['country']
    user=register_tb.objects.filter(name=name,dob=dob,country=country)
    if user.count()>0:
       request.session['id']=user[0].id
       return render(request,'enternewpassword.html',{'abc':user})
    else:
         messages.add_message(request,messages.INFO,'ADDED NEW PASSWORD')
         return redirect('login')

def enternewpasswordAction(request):
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    if newpassword==confirmpassword:
        user=request.session['id']
        users=register_tb.objects.filter(id=user).update(password=newpassword)
        messages.add_message(request,messages.INFO,'UPDATED PASSWORD')
        return render(request,'enternewpassword.html')
    else:
        return redirect('login')

    









   

