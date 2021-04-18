from . import views
from django.urls import path

urlpatterns = [

    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('login',views.login,name='login'),
    path('log',views.log,name='log'),
    path('register',views.register,name='register'),
    path('nregister', views.nregister, name='nregister'),
    path('uhome',views.uhome,name='uhome'),
    path('home',views.home,name='home'),
    path('addtest',views.addtest,name='addtest'),
    path('naddtest', views.naddtest, name='naddtest'),
    path('viewtest',views.viewtest,name='viewtest'),
    path('report',views.report,name='report'),
    path('employee',views.employee,name='employee'),
    path('employeereg',views.employeereg,name='employeereg'),
    path('nereg',views.nereg,name='nereg'),
    path('employeedetails',views.employeedetails,name='employeedetails'),
    path('regusers',views.regusers,name='regusers'),
    path('pviewtest',views.pviewtest,name='pviewtest'),
    path('npviewtest', views.npviewtest, name='npviewtest'),
    path('edit', views.edit, name='edit'),
    path('update', views.update, name='update'),
    path('adminappointments', views.adminappointments, name='adminappointments'),
    path('appointment', views.appointment, name='appointment'),
    path('bookappointment', views.bookappointment, name='bookappointment'),
    path('appohistory', views.appohistory, name='appohistory'),
    path('editemployee', views.editemployee, name='editemployee'),
    path('updateemployee', views.updateemployee, name='updateemployee')

]
