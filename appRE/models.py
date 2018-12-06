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
    password = models.CharField(max_length=50)


