from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator
import datetime

# Create your models here.

class organizer(models.Model):
    organizer_id = models.AutoField(primary_key=True, null=False, unique=True, validators=[MinValueValidator(1), MaxValueValidator(999999), MinLengthValidator(6)])
    organizer_name = models.CharField(max_length=255, null=False, default='Name')
    organizer_address = models.CharField(max_length=255, null=True)
    external = models.BooleanField(null=False, default=False)

class address(models.Model):
    address_id = models.AutoField(primary_key=True, null=False, unique=True, validators=[MinValueValidator(1), MaxValueValidator(999999), MinLengthValidator(6)])
    organizer_id = models.ForeignKey(
        organizer, 
        null=False, 
        on_delete=models.RESTRICT,  
        to_field='organizer_id', 
    )
    address_line1 = models.CharField(max_length=255, null=False, default='Line 1')
    city = models.CharField(max_length=255, null=False, default='City')
    region = models.CharField(max_length=255, null=False, default='Region')
    country = models.CharField(max_length=255, null=False, default='Country')

class contact_person(models.Model):
    contactperson_id = models.AutoField(primary_key=True, null=False, unique=True, validators=[MinValueValidator(1), MaxValueValidator(999999), MinLengthValidator(6)])
    organizer_id = models.ForeignKey(
        organizer, 
        null=False,  
        on_delete=models.RESTRICT,  
        to_field='organizer_id', 
    )
    contact_name = models.CharField(max_length=255, null=False, default='Name')
    contact_email = models.CharField(max_length=255, null=True)
    contact_phone_number = models.CharField(max_length=15, null=False, default='000000000000000')

class activity(models.Model):
    activity_id = models.AutoField(primary_key=True, null=False, unique=True, validators=[MinValueValidator(1), MaxValueValidator(999999), MinLengthValidator(6)])
    organizer_id = models.ForeignKey(
        organizer, 
        null=False, 
        on_delete=models.RESTRICT,  
        to_field='organizer_id', 
    )
    activity_name = models.CharField(max_length=255, null=False, default='Activity')

class activity_hosting(models.Model):
    hosting_id = models.AutoField(primary_key=True, null=False, unique=True, validators=[MinValueValidator(1), MaxValueValidator(999999), MinLengthValidator(6)])
    activity_id = models.ForeignKey(
        activity, 
        null=False, 
        on_delete=models.RESTRICT,  
        to_field='activity_id', 
    )
    date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    expected_participants = models.IntegerField(null=True)

class activity_bookings(models.Model):
    activitybooking_id = models.AutoField(primary_key=True, null=False, unique=True, validators=[MinValueValidator(1), MaxValueValidator(999999), MinLengthValidator(6)])
    activity_id = models.ForeignKey(
        activity, 
        null=False, 
        on_delete=models.RESTRICT,  
        to_field='activity_id', 
    )
    booking_date = models.DateField(null=True)
    attendance = models.IntegerField(null=True)

class participant(models.Model):
    participant_id = models.AutoField(primary_key=True, null=False, unique=True, validators=[MinValueValidator(1), MaxValueValidator(999999), MinLengthValidator(6)])
    name = models.CharField(max_length=255, null=False, default='Name')
    birth_date = models.DateField(null=True)

class participant_type(models.Model):
    participanttype_no = models.AutoField(primary_key=True, null=False, unique=True, validators=[MinValueValidator(1), MaxValueValidator(999999), MinLengthValidator(6)])
    participant_id = models.ForeignKey(
        participant, 
        null=False, 
        on_delete=models.RESTRICT,  
        to_field='participant_id', 
    )
