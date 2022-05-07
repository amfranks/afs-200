from django.db import models

# Create your models here.

class Contact(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    photo = models.CharField(max_length=250)
        
    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.email})"
