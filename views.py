
from django.shortcuts import render
from .models import User,Login,Addtest,Employees,Appointment,Appointmentinfo,Paymentinfo
from datetime import date
import razorpay

def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def log(request):
 try:
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
 except:
        return render(request, 'login.html', {'error': "Invalid Username or Password"})


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
def eviewtest(request):
    data = Addtest.objects.all()
    return render(request, 'eviewtest.html',{'d':data})
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
    apd = date.today()
    test = request.POST.getlist('checks[]')
    print(test)
    data = Appointment(name=name, dob=dob, gender=gender, phone=phone, email=email, datetime=datetime,prescription=prescription,apd=apd,status=0)
    data.save()
    n=data
    for i in test:
        print(i,'fddddddddf')
        insta=Addtest.objects.get(id=i)
        data1 = Appointmentinfo(bookid=n,testid=insta)
        data1.save()
    return render(request, 'appointment.html')


def appointmentinfo(request):

    return render(request, 'appointment.html')

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
def appohistory(request):
    user = request.session['user']
    data = Appointment.objects.filter(email=user)
    return render(request, 'appohistory.html', {'d': data})
def adminappointments(request):
    data = Appointment.objects.filter(status=1)
    return render(request, 'adminappointments.html', {'d': data})
def approvement(request):
    id = request.session['user']
    Appointment.objects.filter(email=id).update(status=0)
    return render(request, 'work.html')
def app(request):
    data = Appointment.objects.filter(status=0)
    return render(request,'pendingappointments.html',{'d':data})
def approve(request):
    id = request.POST['id']
    Appointment.objects.filter(email=id).update(status=1)
    data = Appointment.objects.filter(status=0)
    return render(request,'pendingappointments.html',{'d':data} )
def myprofile(request):
    id=request.session['user']
    data=User.objects.filter(email_id=id)
    return render(request,'myprofile.html',{'data':data})
def pendingappointments(request):
    return render(request,'pendingappointments.html')
def logout(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return render(request,'login.html')
def viewappointment(request):
    user = request.session['user']
    data = Appointment.objects.filter(email=user)
    return render(request, 'viewappointment.html', {'d': data})

def viewappo(request):
    user = request.session['user']
    data = Appointment.objects.filter(email=user)
    return render(request, 'viewappo.html', {'d': data})
def viewappotest(request):
    id = request.POST['id']
    data = Appointmentinfo.objects.filter(bookid=id)
    total=0
    for i in data:
        total+=i.testid.cost
    return render(request, 'viewappotest.html',{'d': data,'t':total})
def adminappointments2(request):
    id = request.POST['id']
    data1 = Appointment.objects.filter(id=id)
    data = Appointmentinfo.objects.filter(bookid=id)
    total = 0
    for i in data:
        total += i.testid.cost
    return render(request, 'adminappointments2.html',{'d': data,'t':data1,'s':total})
def adminreport(request):
    data4 = User.objects.all()
    return render(request,'adminreport.html',{'u': data4})
def employeeappointments(request):
    data = Appointment.objects.filter(status=1)
    return render(request,'employeeappointments.html',{'d': data})
def employeeappointments2(request):
    id = request.POST['id']
    data1 = Appointment.objects.filter(id=id)
    data = Appointmentinfo.objects.filter(bookid=id)
    total = 0
    for i in data:
        total += i.testid.cost
    return render(request, 'employeeappointments2.html',{'d': data,'t':data1,'s':total})
def empprofile(request):
    id=request.session['employee']
    data=Employees.objects.filter(email_id=id)
    return render(request,'empprofile.html',{'data':data})
def esearch(request):
    return render(request, 'search.html')
def search(request):
    n = request.POST['search']
    data = Appointment.objects.filter(name=n)
    return render(request, 'search.html',{'t':data})
def delete(request):
    id = request.POST['id']
    Addtest.objects.filter(id=id).delete()
    data = Addtest.objects.all()
    return render(request, 'viewtest.html', {'d': data})
def edelete(request):
    id = request.POST['id']
    Employees.objects.filter(id=id).delete()
    data = Employees.objects.all()
    return render(request, 'employeedetails.html', {'d': data})



def payment(request):
    user = request.session['user']
    data1 = Appointment.objects.filter(email=user)
    id = request.POST['id']
    data = Appointmentinfo.objects.filter(bookid=id)
    total = 0
    for i in data:
        total += i.testid.cost
    if request.method == 'POST':
        amount = int(total) * 100
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_qalWvQlTe9mOve', 'VKG2NJD9GtnVRqFreKtZqqIw'))
        payment = client.order.create({'amount': amount, 'currency': 'INR',})
        order_id = payment['id']
        order_status = payment['status']

        if order_status == 'created':
            Payment_info = Paymentinfo(

                name=user,
                amount=total,
                order_id=order_id,
                status=0,
                apd=date.today()
            )

            Payment_info.save()
            payment['name'] = user
            return render(request, 'payment.html',{'d': data1, 's': data, 't':total, 'amount': amount, 'user':user,'payment': payment})
    return render(request, 'payment.html',{'d': data1, 's': data, 't':total, 'amount': amount, 'user':user} )

def payment_status(request):
    response = request.POST
    params_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature']
    }

    #client instance
    client = razorpay.Client(auth=('rzp_test_qalWvQlTe9mOve', 'VKG2NJD9GtnVRqFreKtZqqIw'))

    try:
      status = client.utility.verify_payment_signature(params_dict)
      Payment_info = Paymentinfo.objects.get(order_id = response['razorpay_order_id'])
      Payment_info.razorpay_payment_id = response['razorpay_payment_id']
      Payment_info.paid = True
      Payment_info.save()
      return render(request,'payment_status.html', {'status':True})

    except:

      return render(request, 'payment_status.html', {'status':False})



def success(request):
    return render(request, 'success.html')
def receipt(request):
    user = request.session['user']
    data = Paymentinfo.objects.filter(name=user)
    return render(request, 'receipt.html', {'d': data})
