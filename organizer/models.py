from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator

# Create your models here.

class organizer(models.Model):
    organizer_id = models.AutoField(primary_key=True, null=False, unique=True, validators=[MinValueValidator(1), MaxValueValidator(999999), MinLengthValidator(6)])
    organizer_name = models.CharField(max_length=255, null=False, default='Name')
    organizer_address = models.CharField(max_length=255, null=True)
    external = models.BooleanField(null=False, default=False)

class contactperson(models.Model):
    organizer_id = models.ForeignKey(
        organizer, 
        null=False, 
        primary_key=True, 
        on_delete=models.RESTRICT,  
        to_field='organizer_id', 
    )
    contact_name = models.CharField(max_length=255, null=False, default='Name')
    contact_email = models.CharField(max_length=255, null=True)
    contact_phone_number = models.CharField(max_length=15, null=False, default='000000000000000')

