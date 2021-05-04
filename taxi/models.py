from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from phonenumber_field.modelfields import PhoneNumberField

class Taxis(models.Model):
    STATUS = (('YANGI', 'YANGI'),
              ('ESKI', 'ESKI'))

    LICENSE = (('TRUE', 'BOR'),
               ('FALSE', 'YOQ'))

    FULE = (('GAZ', 'GAZ'),
            ('OIL', 'OIL'),
            ('MIXING', 'MIXING'))

    OVEN = (('DAVERNIS', 'DAVERNIS'),
            ('RENT', 'RENT'),
            ('OVEN', 'OVEN'))
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    family_name = models.CharField(max_length=30)
    phone = PhoneNumberField()
    address = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='image/')
    status = models.CharField(max_length=10, default='ESKI', choices=STATUS)
    auto_model = models.CharField(max_length=255)
    auto_marka = models.CharField(max_length=255)
    autogrovnum = models.CharField(max_length=8)
    time=models.TimeField(default=timezone.now())
    auto_license = models.ImageField(default='TRUE', choices=LICENSE, upload_to='image/')
    fule = models.CharField(max_length=10, default='OIL', choices=FULE)
    color = models.CharField(max_length=20)
    year = models.CharField(max_length=4)
    driver_lic = models.ImageField(upload_to='word/')
    passport = models.ImageField(upload_to='image/')
    oven = models.CharField(max_length=10,default='RENT', choices=OVEN)
    created_ad = models.DateTimeField(auto_now_add=True)
    update_ad = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.first_name

    def image_tag(self):
        return mark_safe('<img src="{}" height="5">'.format(self.profle_pic.url))

    image_tag.short_description = 'Passport'

class Staff(models.Model):
     pass
#first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     family_name = models.CharField(max_length=30)
#     phone = models.CharField(max_length=25)
#     address = models.CharField(max_length=255)
