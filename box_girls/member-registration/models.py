from django.db import models

class School(models.Model):
    name = models.CharField(max_length=60)
    school_address = models.TextField()
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    timestamp_added = models.DateTimeField(auto_now_add=True)

class Person(models.Model):
    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    )
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    contact_number = models.BigIntegerField()
    residence_area = models.TextField()
    physical_address = models.TextField()
    in_school = models.NullBooleanField()
    gender = models.CharField(max_length=1, choices=GENDER)
    is_active = models.BooleanField(default=True)
    miscellaneous_contribution = models.TextField()
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    timestamp_added = models.DateTimeField(auto_now_add=True)
    school_details = models.ForeignKey(School, on_delete=models.CASCADE)

class Hobbies(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    timestamp_added = models.DateTimeField(auto_now_add=True)

class Address(models.Model):
    address_1 = models.CharField(max_length=128, blank=False)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=100, blank=False)
    state = models.CharField(max_length=100, blank=False)
    country = models.CharField(max_length=100, blank=False)
    zip_code = models.CharField(max_length=10, default="")



