from django.db import models
from localflavor.us.models import USStateField, USZipCodeField

from bolo_users.models import User

class BoloCategory(models.Model):
    name = models.CharField(max_length=128)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class BoloStatus(models.Model):
    name = models.CharField(max_length=128)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Bolo(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    category = models.ForeignKey(BoloCategory, on_delete=models.PROTECT)
    status = models.ForeignKey(BoloStatus, on_delete=models.PROTECT)

    video_url = models.URLField(blank=True, null=True)
    description = models.TextField()

    address_1 = models.CharField(max_length=128, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    state = USStateField(blank=True, null=True)
    zip_code = USZipCodeField(max_length=5, blank=True, null=True)

    reported_date = models.DateField()
    reported_time = models.TimeField()
    
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_internal = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class BoloImage(models.Model):
    bolo = models.ForeignKey(Bolo, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='bolo_images')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class BoloSubscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bolo = models.ForeignKey(Bolo, related_name="subscribed_bolos", on_delete=models.CASCADE)
    subscribed_on = models.DateTimeField(auto_now_add=True)
