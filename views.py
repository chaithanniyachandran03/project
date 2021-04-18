from django.shortcuts import render
from .models import User,Login,Addtest,Employees,Appointment,Appointmentinfo
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def log(request):
    email = request.POST['email']
    password = request.POST['password']
    m = Login.objects.get(email=email,password=password)
    if m.status == 1:
        request.session['user'] = m.email
        return render(request, 'uhome.html')
    elif m.status == 2:
        request.session['employee'] = m.email
        return render(request, 'employee.html')
    elif m.status == 0:

        return render(request, 'home.html')
    else:
        return render(request, 'login.html', {'error':"Your username and password didn't match."})

def register(request):
    return render(request, 'register.html')

def nregister(request):
    name = request.POST['name']
    address = request.POST['address']
    dob = request.POST['dob']
    gender = request.POST['gender']
    phone = request.POST['phone']
    email = request.POST['email']
    password = request.POST['password']
    data = User(name=name, address=address, dob=dob, gender=gender, phone=phone, email_id=email)
    data.save()
    data1 = Login(email=email,password=password,status=1)
    data1.save()
    return render(request,'login.html')
def uhome(request):
    data = Addtest.objects.all
    return render(request, 'uhome.html',{'t':data})
def addtest(request):
    return render(request, 'addtest.html')
def naddtest(request):
    name = request.POST['name']
    cost = request.POST['cost']
    description = request.POST['description']
    sample = request.POST['sample']
    testdata = Addtest(name=name, cost=cost, description=description, sample=sample)
    testdata.save()
    return render(request, 'addtest.html')
def viewtest(request):
    data = Addtest.objects.all()
    return render(request, 'viewtest.html',{'d':data})
def report(request):
    return render(request, 'report.html')
def employee(request):
    return render(request, 'employee.html')
def employeereg(request):
    return render(request, 'employeereg.html')

def nereg(request):
    name = request.POST['name']
    photo = request.FILES['file']
    address = request.POST['address']
    age = request.POST['age']
    gender = request.POST['gender']
    phone = request.POST['phone']
    email = request.POST['email']
    password = request.POST['password']
    data2 = Employees(name=name,photo=photo, address=address, age=age, gender=gender, phone=phone, email_id=email)
    data2.save()
    data2 = Login(email=email,password=password,status=2)
    data2.save()
    return render(request,'employeereg.html')
def employeedetails(request):
    data3 = Employees.objects.all()
    return render(request, 'employeedetails.html',{'d':data3})
def regusers(request):
    data4 = User.objects.all()
    return render(request, 'regusers.html',{'u':data4})
def pviewtest(request):
    return render(request, 'pviewtest.html')
def npviewtest(request):
    n = request.POST['id']
    data = Addtest.objects.filter(id=n)
    return render(request, 'pviewtest.html',{'t':data})
def edit(request):
    id = request.POST['id']
    data = Addtest.objects.get(id=id)
    return render(request, 'edit.html',{'data':data})
def update(request):
    id = request.POST['id']
    data = Addtest.objects.get(id=id)
    data.name = request.POST['name']
    data.cost = request.POST['cost']
    data.description = request.POST['description']
    data.sample = request.POST['sample']
    data.save()
    data1 = Addtest.objects.all()
    return render(request, 'viewtest.html',{'d':data1})
def adminappointments(request):
    return render(request, 'adminappointments.html')
def appointment(request):
    data = Addtest.objects.all()
    return render(request, 'appointment.html',{'d': data})
def bookappointment(request):
    name = request.POST['name']
    dob = request.POST['dob']
    gender = request.POST['gender']
    phone = request.POST['phone']
    email = request.POST['email']
    datetime = request.POST['datetime']
    prescription = request.FILES['file']
    test = request.POST.getlist('checks[]')
    print(test)
    data = Appointment(name=name, dob=dob, gender=gender, phone=phone, email=email, datetime=datetime,prescription=prescription,tests=test)
    data.save()
    return render(request, 'appointment.html')
def appointmentinfo(request):
    id = request.POST['id']
    Addtest.objects.get(id=id)

    return render(request,'appointment.html')
def appohistory(request):
    return render(request,'appohistory.html')
def editemployee(request):
    id = request.POST['id']
    data = Employees.objects.get(id=id)
    return render(request, 'editemployee.html',{'data':data})
def updateemployee(request):
    id = request.POST['id']
    data = Employees.objects.get(id=id)
    data.name = request.POST['name']
    data.photo = request.FILES['file']
    data.address = request.POST['address']
    data.age = request.POST['age']
    data.gender = request.POST['gender']
    data.phone = request.POST['phone']
    data.email_id = request.POST['email']
    data.save()
    data1 = Employees.objects.all()
    return render(request, 'employeedetails.html',{'d':data1})

