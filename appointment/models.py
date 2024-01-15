from django.db import models
from patient.models import Patient
from doctor.models import Doctor , AvailableTime
# Create your models here.
APPOINTMENT_STATUS = [
    ('Complited','Complited'),
    ('Pending','Pending'),
    ('Running','Running'),
]
APPOINTMENT_TYPE = [
    ('Offline','Offline'),
    ('Online','Online'),
]

class Appointment(models.Model):
    patient = models.ForeignKey(Patient,on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete = models.CASCADE)
    appointment_types = models.CharField(choices=APPOINTMENT_TYPE , max_length=16)
    appointment_status = models.CharField(choices=APPOINTMENT_STATUS , default = 'Pending' ,max_length=16)

    symptom = models.TextField()
    time = models.ForeignKey(AvailableTime,on_delete = models.CASCADE)
    cancle = models.BooleanField(default = False)

    def __str__(self):
        return f"Doctor: {self.doctor.user.first_name} Patient: {self.patient.user.first_name}"