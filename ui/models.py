from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw



class Entry(models.Model):
    First_Name = models.CharField(max_length=25, null=True)
    Last_Name = models.CharField(max_length=25, null=True)
    Name_of_animal = models.CharField(max_length=25, null=True)
    Type_of_animal = models.CharField(max_length=10, null=True)
    Sex = models.CharField(max_length=10, null=True)
    Age = models.CharField(max_length=10, null=True)
    Breed = models.CharField(max_length=50, null=True)
    Color = models.CharField(max_length=40, null=True)
    Groomer = models.CharField(max_length=40, null=True, blank=True)
    Weight = models.CharField(max_length=40, null=True)
    DCV_DLX= models.CharField(max_length=40, null=True, blank=True)
    GCD = models.CharField(max_length=40, null=True, blank=True)
    Home = models.CharField(max_length=40, null=True, blank=True)
    Cell = models.CharField(max_length=40, null=True, blank=True)
    Work = models.CharField(max_length=40, null=True, blank=True)
    Vet= models.CharField(max_length=40, null=True, blank=True)
    Emer = models.CharField(max_length=40, null=True, blank=True)
    DHLPP = models.CharField(max_length=40, null=True)
    Rabies = models.CharField(max_length=40, null=True)
    Bordetella = models.CharField(max_length=40, null=True)
    Remarks = models.CharField(max_length=40, null=True, blank=True)
    Our_or_own_food = models.CharField(max_length=40, null=True)
    Meds = models.CharField(max_length=40, null=True, blank=True)
    Rot= models.CharField(max_length=40, null=True, blank=True)
    Starts= models.CharField(max_length=40, null=True, blank=True)
    Ends= models.CharField(max_length=40, null=True, blank=True)
    Mrn= models.CharField(max_length=40, null=True, blank=True)
    Eve= models.CharField(max_length=40, null=True, blank=True)
    Dosage= models.CharField(max_length=40, null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #qr codes
    qrcode=models.ImageField(upload_to='qr_codes', blank=True)


    def get_absolute_url(self):
        return reverse('entry-detail', kwargs={'pk': self.pk})