from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django_dnf.fields import DomainNameField
from localflavor.us.models import USStateField, USZipCodeField
from phonenumber_field.modelfields import PhoneNumberField

class Agency(models.Model):

    name = models.CharField(max_length=100)
    acronym = models.CharField(max_length=10, default=None, null=True)
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

    class Meta:
        verbose_name_plural = 'Agencies'

    def __str__(self):
        return self.name

class Unit(models.Model):

    name = models.CharField(max_length=128)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Rank(models.Model):

    name = models.CharField(max_length=128)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class UserManager(BaseUserManager):
    
    def create_user(self, username, email, first_name, last_name, phone, badge, agency, unit, rank, password = None):

        user = self.model(
            username = username,
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            badge = badge,
            agency = agency,
            unit = unit,
            rank = rank,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, username, email, first_name, last_name, password):

        user = self.create_user(
            username = username,
            password = password,
            email = email,
            first_name = first_name,
            last_name = last_name,
            phone = None,
            badge = None,
            agency = None,
            unit = None,
            rank = None,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = PhoneNumberField(blank=True, null=True)
    badge = models.CharField(max_length=10, blank=True, null=True)
    agency = models.ForeignKey(Agency, on_delete=models.PROTECT, blank=True, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT, blank=True, null=True)
    rank = models.ForeignKey(Rank, on_delete=models.PROTECT, blank=True, null=True)

    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        models.Model.save(self, *args, **kwargs)

class AgencySubscribing(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    agency = models.ForeignKey(Agency, related_name="subscribed_agencies", on_delete=models.CASCADE)
    subscribed_on = models.DateTimeField(auto_now_add=True)
