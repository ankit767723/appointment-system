# appointments/models.py

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    # Add other doctor-related fields like schedule, location, etc.

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    patient_name = models.CharField(max_length=255)

