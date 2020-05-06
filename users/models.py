from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    Role_name = models.CharField(max_length=50)

# Create your models here.
class Profile(models.Model):
    role = models.ForeignKey(Role, null=False, on_delete=models.PROTECT)
    user = models.ForeignKey(User, null=False, on_delete=models.PROTECT)

#identificacion (1= identification card, 2= Foreign ID, 3= passport)
class Type_identity(models.Model):
    type = models.CharField(max_length=15)

#Create model USer data
class User_data(models.Model):
    type_identity = models.ForeignKey(Type_identity, null=False, on_delete=models.PROTECT)
    identification = models.CharField(max_length=20, null=True)
    Phone = models.IntegerField(null=True)
