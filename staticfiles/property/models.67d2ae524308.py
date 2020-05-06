#encoding:utf-8 <- Esta línea permite usar tíldes y caracteres especiales
from django.db import models #Clase con la descripción de modelos
from django.contrib.auth.models import User
import datetime

#Create model Type property
#Properties_type (1= apartment, 2=house 3=local 4=farm)
class Property_type(models.Model):
    name = models.CharField(max_length=30)

# Create model Property State
class Property_state(models.Model):
    name = models.CharField(max_length=50)

# Create model Property Model
class Property(models.Model):
    #string data(cadena), max_length 50
    name = models.CharField(max_length=50, null=False)
    price = models.DecimalField(max_digits=8, decimal_places=0, null= False)
    city = models.CharField(max_length=30)
    neighborhood = models.CharField(max_length=50)
    address = models.CharField(max_length=120)
    length = models.DecimalField(max_digits=4, decimal_places=1)
    antiquity = models.IntegerField()
    floors = models.IntegerField()
    amount_rooms = models.IntegerField()
    bathrooms=models.IntegerField()
    stract = models.IntegerField()
    urlimage = models.ImageField(null=True,upload_to='property/%Y/%m/%d')
    description = models.CharField(max_length=600)
    property_type = models.ForeignKey(Property_type, null=False, on_delete=models.PROTECT)
    property_state = models.ForeignKey(Property_state, null=False, on_delete=models.PROTECT)
    available = models.BooleanField(default=True)


# Create model Property type Management
class Type_management(models.Model):
    name = models.CharField(max_length=50)

# Create model Property Management
class Property_management(models.Model):
    start_date = models.DateTimeField(null=False)
    end_date =  models.DateTimeField(null=False)
    #current_state (1= 1 to 5  years old 2= 5 to 10 yeras old  3= 10 to 20 years old)
    current_state = models.BooleanField(null= False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    contract_number = models.IntegerField()
    observations = models.CharField(max_length=600)
    user = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
    property = models.ForeignKey(Property, null=False, on_delete=models.PROTECT)
    type_management = models.ForeignKey(Type_management, null=False, on_delete=models.PROTECT)
