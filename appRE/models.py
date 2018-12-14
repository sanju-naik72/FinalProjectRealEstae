from django.db import models

from django.db import models

from django.db import models

class State(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

class City(models.Model):
    idno =  models.IntegerField(primary_key=True)
    s_name = models.ForeignKey(State,on_delete=models.CASCADE)
    c_name = models.CharField(max_length=50)

class Locality(models.Model):
    idno = models.IntegerField(primary_key=True)
    c_name = models.ForeignKey(City,on_delete=models.CASCADE)
    loc_name = models.CharField(max_length=50)
    pincode = models.IntegerField()

class Property_name(models.Model):
    idno = models.IntegerField(primary_key=True)
    loc_name = models.ForeignKey(Locality,on_delete=models.CASCADE)
class property(models.Model):
    Customer_Name=models.CharField(max_length=100)
    name=models.CharField(max_length=500)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    contact_number=models.IntegerField()
    pincode=models.IntegerField()
    Customer_Email=models.EmailField(max_length=500,default=None)
    price=models.DecimalField(max_digits=10,decimal_places=2,default=None)


class Sales(models.Model):
    name = models.CharField(max_length=50)
    contact_no = models.IntegerField()
    email_id = models.EmailField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    Age = models.IntegerField()
    gender = models.CharField(max_length=10)

class Suggestion(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contact_no = models.IntegerField()
    message = models.CharField(max_length=500)

class UserRegister(models.Model):
    name = models.CharField(max_length=50)
    contact_no = models.IntegerField()
    email_id = models.EmailField(max_length=100, primary_key=True)
    gender = models.CharField(max_length=10,default=None)
    age = models.IntegerField(default=None)
    password = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50,default=None)
    salary = models.DecimalField(max_digits=10, decimal_places=2,default=0)


