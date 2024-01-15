from django.db import models

# Create your models here.
class Service(models.Model):
    image =models.ImageField(upload_to="service/image/")
    name = models.CharField(max_length = 30)
    description = models.TextField(blank=True,null=True)