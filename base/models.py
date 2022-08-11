from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
import base.choices

# Create your models here.

class Common(models.Model):
    license_id = models.IntegerField()
    user_created_id = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    user_edit_id = models.IntegerField(null=True, blank=True)
    date_edit = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, blank=True, default='')
  
    class Meta:
        abstract = True  


class License(Common):
    license_key = models.CharField(max_length=50, unique=True)
    desc = models.CharField(max_length=40)
    num_licenses = models.IntegerField(default=3)
    user_type = models.CharField(max_length=1, default='A')

    def __str__(self) -> str:
        return self.desc


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    #bio = models.TextField(null=True)
    user_type  = models.CharField(max_length=1, null=True,  default='U')
    image_file = models.ImageField(null=True, default="avatar.svg", upload_to="users/")
    license_id = models.IntegerField(default=1)
    status = models.CharField(max_length=1, default='A')
    modo_apariencia = models.CharField(max_length=1, choices = [('0', 'Claro'), ('1', 'Oscuro')], default='0')

    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    pass

