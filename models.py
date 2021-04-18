from django.db import models
class User(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    dob = models.CharField(max_length=30)
    gender = models.CharField(max_length=2)
    phone = models.IntegerField()
    email_id = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    cpassword = models.CharField(max_length=30)
class Login(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    status = models.IntegerField()
class Addtest(models.Model):
    name = models.CharField(max_length=30)
    cost = models.IntegerField()
    description = models.CharField(max_length=30)
    sample = models.CharField(max_length=30)
class Employees(models.Model):
    name = models.CharField(max_length=30)
    photo = models.FileField()
    address = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=2)
    phone = models.IntegerField()
    email_id = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
class Appointment(models.Model):
    name = models.CharField(max_length=30)
    dob = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    datetime = models.CharField(max_length=30)
    prescription = models.FileField()
    tests = models.CharField(max_length=2022)
class Appointmentinfo(models.Model):
    amount = float()




