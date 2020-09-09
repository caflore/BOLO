from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django_dnf.fields import DomainNameField
from localflavor.us.models import USStateField, USZipCodeField, PhoneNumberField

class UserManager(BaseUserManager):
    pass

class User(AbstractBaseUser):
    
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = PhoneNumberField()
    badge = models.CharField(max_length=10)
    agency = models.ForeignKey(Agency, on_delete=models.PROTECT)
    unit = models.ForeignKey(Units, on_delete=models.PROTECT)
    rank = models.ForeignKey(Rank, on_delete=models.PROTECT)

    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

class Agency(models.Model):

    name = models.CharField(max_length=100)
    domain = DomainNameField()
    phone = PhoneNumberField()
    agency_logo = models.ImageField(default='default_agency_logo.png', upload_to='agency_logos')
    agency_sheild = models.ImageField(default='default_agency_sheild.png', upload_to='agency_sheilds')    
    agency_watermark = models.ImageField(upload_to='agency_watermarks')
    
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64)
    state = USStateField()
    zip_code = USZipCodeField(max_length=5)

    is_active = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class AgencySubscribing(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    agency = models.ForeignKey(Agency, related_name="subscribed_agencies", on_delete=CASADE)
    subscribed_on = models.DateTimeField(auto_now_add=True)

class Unit(models.Models):

    name = models.CharField(max_length=128)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class Rank(models.Model):

    name = models.CharField(max_length=128)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
