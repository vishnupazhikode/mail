from django.shortcuts import render,redirect
from siteadmin.models import *
from user.models import *
from django.contrib import messages
import datetime
from django.http import JsonResponse

# Create your views here.


def register(request):
    country=country_tb.objects.all()
    state=state_tb.objects.all()
    hobby=hobbyname_tb.objects.all()
    return render(request,'register.html',{'country':country,'state':state,'hobby':hobby})
def getstate(request):
    cid=request.GET['country_id']
    state=state_tb.objects.filter(countryid=cid)
    return render(request,'getstate.html',{'state':state})

def registerAction(request):
    name=request.POST['name']
    address=request.POST['address']
    gender=request.POST['gender']
    dob=request.POST['dob']
    phonenumber=request.POST['phonenumber']
    country=request.POST['country']
    state=request.POST['state']
    username=request.POST['username']
    password=request.POST['password']
    securityquestion=request.POST['securityquestion']
    answer=request.POST['answer']
    user=register_tb(name=name,address=address,gender=gender,dob=dob,phonenumber=phonenumber,country=country,state=state,username=username+'@mymail.com',password=password,securityquestion=securityquestion,answer=answer)
    user.save()
    hobbi=request.POST.getlist('hobby')
    for vid in hobbi:
        hobby=hobby_tb(userid_id=user.id,hobbyid_id=vid)
        hobby.save()
        messages.add_message(request,messages.INFO,"sucess")
    return redirect('register')

def sendmessage(request):
    return render(request,'sendmessage.html')
def sendmessageAction(request):
    sender=request.session['id']
    reciver=request.POST['recivername']
    qwe=register_tb.objects.get(username=reciver)
    
    subject=request.POST['subject']
    message=request.POST['message']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    user=message_tb(senderid_id=sender,reciverid=qwe,subject=subject,message=message,date=date,time=time)
    user.save()
    messages.add_message(request,messages.INFO,'message send')
    return redirect('sendmessage')

def checkusername(request):
    usern=request.GET['username']
    user=register_tb.objects.filter(username=usern)
    if len(user)>0:
        msg="exist"
    else:
        msg="not exist"
    return JsonResponse({'valid':msg})

def viewsendermessage(request):
    qwe=request.session['id']
    status=['pending','deletedbyreciver']
    oi=message_tb.objects.filter(senderid=qwe,status__in=status)
    return render(request,'viewsendermessage.html',{'send':oi})
def delete(request,id):
    user=message_tb.objects.filter(id=id)
    status=user[0].status
    if status=='deleted by reciver':
        wer=message_tb.objects.filter(id=id).delete()
        return redirect('viewsendermessage')
    if status=='pending':
        asd=message_tb.objects.filter(id=id).update(status='deleted by sender')
    return redirect('viewsendermessage')
    
   
def inbox(request):
    asd=request.session['id']
    status=['pending','deletedbysender']
    #user=message_tb.objects.filter(reciverid=asd,status__in=status)
    agefactor=custumeragefactor_tb.objects.filter(userid=asd)
    for factor in agefactor:
        age=message_tb.objects.filter(reciverid=asd,filterstatus='pending',message__icontains=factor.factorid.factor).exclude(senderid__in=blacklist_tb.objects.filter(userid=asd).values('contactid')).update(filterstatus="filtered")
        print(factor.factorid.factor)
    seasonfactor=custumerseasoncountry_tb.objects.filter(userid=asd)
    for factor in seasonfactor:
        season=message_tb.objects.filter(reciverid=asd,filterstatus='pending',message__icontains=factor.factorid.factor).exclude(senderid__in=blacklist_tb.objects.filter(userid=asd).values('contactid')).update(filterstatus="filtered")

    hobbyfactor=custumerhobbyfactor_tb.objects.filter(userid=asd)
    for factor in hobbyfactor:
        hobby=message_tb.objects.filter(reciverid=asd,filterstatus='pending',message__icontains=factor.factorid.factorname).exclude(senderid__in=blacklist_tb.objects.filter(userid=asd).values('contactid')).update(filterstatus="filtered")

    contact=contact_tb.objects.filter(userid=asd)
    for c in contact:
        con=message_tb.objects.filter(reciverid=asd,filterstatus='pending',senderid=c.contactid).update(filterstatus='filtered')

    user=message_tb.objects.filter(reciverid=asd,status__in=status,filterstatus='filtered').exclude(id__in=trash_tb.objects.filter(reciverid=asd).values('messageid_id'))
    return render(request,'inbox.html',{'inbox':user})


   
def checkreciver(request):
    reciver=request.GET['user']
    user=register_tb.objects.filter(username=reciver)
    if len(user)>0:
        msg="exist"
    else:
        msg="not exist"
    return JsonResponse({'valid':msg})
def movetotrashAction(request):
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    box=request.POST.getlist('checkbox')
    for vid in box:
        re=request.session['id']
        acc=message_tb.objects.get(id=vid)
        user=trash_tb(date=date,time=time,messageid=acc,reciverid_id=re)
        user.save()
        messages.add_message(request,messages.INFO,"added")
    return redirect('inbox')

def viewtrassh(request):
    abf=request.session['id']
    trash=trash_tb.objects.filter(reciverid=abf)
    return render(request,"viewtrash.html",{'tra':trash})
def deletetrassh(request,id):
    fgh=trash_tb.objects.filter(id=id)
    asd=message_tb.objects.filter(id=fgh[0].messageid_id)
    status=asd[0].status
    if status=='pending':
        xya=message_tb.objects.filter(id=fgh[0].messageid_id).update(status="deleted by reciver")
        swe=trash_tb.objects.filter(id=id).delete()
    return redirect('viewtrassh')

def forward(request,id):
    rew=message_tb.objects.filter(id=id)
    return render(request,"forward.html",{'fore':rew})
def forwardAction(request):
    put=request.session['id']
    rec=request.POST['reciver']
    qwe=register_tb.objects.get(username=rec)
    subject=request.POST['subject']
    message=request.POST['message']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    user=message_tb(senderid_id=put,reciverid=qwe,subject=subject,message=message,date=date,time=time)
    user.save()
    messages.add_message(request,messages.INFO,'forwarded')
    return redirect('inbox')
def reply(request,id):
    asd=message_tb.objects.filter(id=id)
    return render(request,"reply.html",{'reply':asd})
def replyAction(request):
    ert=request.session['id']
    art=request.POST['reciver']
    reciver=register_tb.objects.get(username=art)
    subject=request.POST['subject']
    message=request.POST['message']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    user=message_tb(senderid_id=ert,reciverid=reciver,subject=subject,message=message,date=date,time=time)
    user.save()
    messages.add_message(request,messages.INFO,'replied')
    return redirect('inbox')

def addcontact(request):
    return render(request,"addcontact.html")
def addcontactAction(request):
    ser=request.session['id']
    abc=request.POST['contactabc']
    rec=register_tb.objects.get(username=abc)
    name=request.POST['name']
    remark=request.POST['remark']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    user=contact_tb(userid_id=ser,contactid=rec,name=name,remark=remark,date=date,time=time)
    user.save()
    messages.add_message(request,messages.INFO,'added')
    return redirect('addcontact')

def blacklist(request):
    return render(request,'blacklist.html')
def blacklistAction(request):
    reg=request.session['id']
    contact=request.POST['contactid']
    ert=register_tb.objects.get(username=contact)
    name=request.POST['name']
    remark=request.POST['remark']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    user=blacklist_tb(userid_id=reg,contactid=ert,name=name,remark=remark,date=date,time=time)
    user.save()
    messages.add_message(request,messages.INFO,"added to blacklist")
    return redirect('blacklist')

def viewcontact(request):
    azx=request.session['id']
    contact=contact_tb.objects.filter(contactid=azx)
    return render(request,"viewcontact.html",{'cont':contact})
def deletecontact(request,id):
    ddd=contact_tb.objects.filter(id=id).delete()
    return redirect('viewcontact')

def viewblacklist(request):
    bzx=request.session['id']
    black=blacklist_tb.objects.filter(contactid=bzx)
    return render(request,"viewblacklist.html",{'blck':black})
def deleteblacklist(request,id):
    user=blacklist_tb.objects.filter(id=id).delete()
    return redirect('viewblacklist')

def movetoblacklist(request,id):
    qq=request.session['id']
    dd=contact_tb.objects.filter(id=id)
    remark=dd[0].remark
    name=dd[0].name
    contact=dd[0].contactid
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    rr=blacklist_tb(userid_id=qq,remark=remark,name=name,contactid=contact,date=date,time=time)
    rr.save()
    dd.delete()
    messages.add_message(request,messages.INFO,'moved')
    return redirect('viewcontact')
def custumerhobbyfactor(request):
    uyy=request.session['id']
    abc=hobby_tb.objects.filter(id=uyy)
    return render(request,'custumerhobbyfactor.html',{'ho':abc})
def gethobbyfactor(request):
    hid=request.GET['name']
    factor=hobbyfactor_tb.objects.filter(hobbyid=hid)
    return render(request,'gethobbyfactor.html',{'fact':factor})
def custumerhobbyfactorAction(request):
    us=request.session['id']
    hobby=request.POST['hobby']
    fac=request.POST['factor']
    user=custumerhobbyfactor_tb(userid_id=us,hobbyid_id=hobby,factorid_id=fac)
    user.save()
    messages.add_message(request,messages.INFO,"added")
    return redirect('custumerhobbyfactor')
def custumeragefactor(request):
    art=request.session['id']
    abc=register_tb.objects.filter(id=art)
    birthdate=abc[0].dob
    cde=birthdate.split('-')
    efg=cde[0]
    date=datetime.date.today()
    zyx=date.year
    yxo=int(zyx)-int(efg)
    za=agefactor_tb.objects.filter(minage__lte=yxo,maxage__gte=yxo)
    return render(request,'custumeragefactor.html',{'cag':za})
def custumeragefactorAction(request):
    custemer=request.session['id']
    factor=request.POST['agefactor']
    abc=custumeragefactor_tb(userid_id=custemer,factorid_id=factor)
    abc.save()
    messages.add_message(request,messages.INFO,'added sucessfully')
    return redirect('custumeragefactor')

def custumerseasoncountry(request):
    use=request.session['id']
    ert=register_tb.objects.filter(id=use)
    country=ert[0].country
    state=ert[0].state
    date=datetime.date.today()
    month=date.month
    season=seasoncountry_table.objects.filter(countryid=country,stateid=state,months=month)
    return render(request,'custumerseasoncountry.html',{'uff':season})
def custumerseasoncountryAction(request):
    usr=request.session['id']
    factor=request.POST['seasonfactor']
    user=custumerseasoncountry_tb(userid_id=usr,factorid_id=factor)
    user.save()
    messages.add_message(request,messages.INFO,'added sucessfully')
    return redirect('custumerseasoncountry')

def viewspam(request):
    use=request.session['id']
    status=['pending','deleted by sender']
    rel=message_tb.objects.filter(reciverid=use,status__in=status,filterstatus='pending')
    
    return render(request,'viewspam.html',{'spaam':rel})
def deletespam(request,id):
    spam=message_tb.objects.filter(id=id)
    status=spam[0].status
    if status=='deleted by sender':
        abc=message_tb.objects.filter(id=id).delete()
        return redirect('viewspam')
    if status=='pending':
        wer=message_tb.objects.filter(id=id).update(status='deletd by reciver')
    return redirect('viewspam')

def edit(request):
    u=request.session['id']
    us=register_tb.objects.filter(id=u)
    country=country_tb.objects.all()
    state=state_tb.objects.all()
    hobby=hobbyname_tb.objects.all()
    ho=hobby_tb.objects.filter(userid=u)
    return render(request,'edit.html',{'user':us,'country':country,'state':state,'hobby':hobby,'ho':ho})
def editAction(request):
    us=request.session['id']
    users=register_tb.objects.get(id=us)
    name=request.POST['name']
    address=request.POST['address']
    gender=request.POST['gender']
    dob=request.POST['dob']
    phonenumber=request.POST['phonenumber']
    country=request.POST['country']
    state=request.POST['state']
    username=request.POST['username']
    password=request.POST['password']
    securityquestion=request.POST['securityquestion']
    answer=request.POST['answer']
    user=register_tb.objects.filter(id=us).update(name=name,address=address,gender=gender,dob=dob,phonenumber=phonenumber,country=country,state=state,username=username,password=password,securityquestion=securityquestion,answer=answer)
    oldhobby=hobby_tb.objects.filter(userid=us).delete()
    hobbis=request.POST[ "hobby"]
    for vid in hobbis:
        ho=hobbyname_tb.objects.get(id=vid)
        hobby=hobby_tb(userid=users,hobbyid=ho)
        hobby.save()
        messages.add_message(request,messages.INFO,"updated")
    return redirect('edit')








    










