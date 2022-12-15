"""spammail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from siteadmin import views as adminview
from user import views as userview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',adminview.index,name="index"),
    path('login/',adminview.login,name="login"),
    path('loginAction/',adminview.loginAction,name="loginAction"),
    path('addhobby/',adminview.addhobby,name="addhobby"),
    path('addhobbyAction/',adminview.addhobbyAction,name="addhobbyAction"),
    path('register/',userview.register,name="register"),
    path('getstate/',userview.getstate,name="getstate"),   
    path('registerAction/',userview.registerAction,name="registerAction"),
    path('sendmessage/',userview.sendmessage,name="sendmessage"),
    path('sendmessageAction/',userview.sendmessageAction,name="sendmessageAction"),
    path('factor/',adminview.factor,name="factor"),
    path('factorAction/',adminview.factorAction,name="factorAction"),
    path('checkusername/',userview.checkusername,name="checkusername"),
    path('season/',adminview.season,name="season"),
    path('seasonAction/',adminview.seasonAction,name="seasonAction"),
    path('seasonfactor/',adminview.seasonfactor,name="seasonfactor"),
    path('seasonfactorAction/',adminview.seasonfactorAction,name="seasonfactorAction"),
    path("getfactor/",adminview.getfactor,name="getfactor"),
    path('seasoncountry/',adminview.seasoncountry,name="seasoncountry"),
    path('seasoncountryAction/',adminview.seasoncountryAction,name="seasoncountryAction"),
    path('agefactor/',adminview.agefactor,name="agefactor"),
    path('agefactorAction/',adminview.agefactorAction,name="agefactorAction"),
    path('viewsendermessage/',userview.viewsendermessage,name="viewsendermessage"),
    path("delete<int:id>/",userview.delete,name="delete"),
    path('inbox/',userview.inbox,name="inbox"),
    path('checkreciver/',userview.checkreciver,name="checkreciver"),
    path('movetotrashAction/',userview.movetotrashAction,name="movetotrashAction"),
    path('viewtrassh/',userview.viewtrassh,name="viewtrassh"),
    path('deletetrassh<int:id>/',userview.deletetrassh,name="deletetrassh"),
    path('forward<int:id>/',userview.forward,name="forward"),
    path('forwardAction/',userview.forwardAction,name="forwardAction"),
    path('reply<int:id>/',userview.reply,name="reply"),
    path('replyAction/',userview.replyAction,name="replyAction"),
    path('addcontact/',userview.addcontact,name="addcontact"),
    path('addcontactAction/',userview.addcontactAction,name="addcontactAction"),
    path('blacklist/',userview.blacklist,name="blacklist"),
    path('blacklistAction/',userview.blacklistAction,name="blacklistAction"),
    path('viewcontact/',userview.viewcontact,name="viewcontact"),
    path('deletecontact<int:id>/',userview.deletecontact,name="deletecontact"),
    path('viewblacklist/',userview.viewblacklist,name="viewblacklist"),
    path('deleteblacklist<int:id>/',userview.deleteblacklist,name="deleteblacklist"),
    path('movetoblacklist<int:id>/',userview.movetoblacklist,name='movetoblacklist'),
    path('custumerhobbyfactor/',userview.custumerhobbyfactor,name='custumerhobbyfactor'),
    path('gethobbyfactor/',userview.gethobbyfactor,name="gethobbyfactor"),
    path('custumerhobbyfactorAction/',userview.custumerhobbyfactorAction,name="custumerhobbyfactorAction"),
    path('custumeragefactor/',userview.custumeragefactor,name='custumeragefactor'),
    path('custumeragefactorAction/',userview.custumeragefactorAction,name="custumeragefactorAction"),
    path('custumerseasoncountry/',userview.custumerseasoncountry,name='custumerseasoncountry'),
    path('custumerseasoncountryAction/',userview.custumerseasoncountryAction,name='custumerseasoncountryAction'),
    path('viewspam/',userview.viewspam,name="viewspam"),
    path('deletespam<int:id>/',userview.deletespam,name='deletespam'),
    path('forgotpassword/',adminview.forgotpassword,name="forgotpassword"),
    path('forgotpasswordAction/',adminview.forgotpasswordAction,name="forgotpasswordAction"),
    path('newpasswordAction/',adminview.newpasswordAction,name="newpasswordAction"),
    path('enternewpasswordAction/',adminview.enternewpasswordAction,name='enternewpasswordAction'),
    path('edit/',userview.edit,name="edit"),
    path('editAction/',userview.editAction,name='editAction')




]
