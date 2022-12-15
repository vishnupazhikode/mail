from django.db import models

# Create your models here.
class country_tb(models.Model):
    countryname=models.CharField(max_length=20)
class state_tb(models.Model):
    statename=models.CharField(max_length=20)
    countryid=models.ForeignKey(country_tb,on_delete=models.CASCADE)

class register_tb(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    phonenumber=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    securityquestion=models.CharField(max_length=20)
    answer=models.CharField(max_length=20)

class hobby_tb(models.Model):
    userid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    hobbyid=models.ForeignKey('siteadmin.hobbyname_tb',on_delete=models.CASCADE)

class message_tb(models.Model):
    senderid=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name='sender')
    reciverid=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name='reciver')
    subject=models.CharField(max_length=20)
    message=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    status=models.CharField(max_length=20,default='pending')
    filterstatus=models.CharField(max_length=20,default='pending')
class trash_tb(models.Model):
    messageid=models.ForeignKey(message_tb,on_delete=models.CASCADE)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    reciverid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
class contact_tb(models.Model):
    userid=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name='user')
    contactid=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name='contact')
    name=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    remark=models.CharField(max_length=20)
class blacklist_tb(models.Model):
    userid=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name='user1')
    contactid=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name='contact1')
    name=models.CharField(max_length=20)
    remark=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)

class custumerhobbyfactor_tb(models.Model):
    userid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    hobbyid=models.ForeignKey('siteadmin.hobbyname_tb',on_delete=models.CASCADE)
    factorid=models.ForeignKey('siteadmin.hobbyfactor_tb',on_delete=models.CASCADE)

class custumeragefactor_tb(models.Model):
    userid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    factorid=models.ForeignKey('siteadmin.agefactor_tb',on_delete=models.CASCADE)

class custumerseasoncountry_tb(models.Model):
    userid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    factorid=models.ForeignKey('siteadmin.seasonfactor_tb',on_delete=models.CASCADE)
