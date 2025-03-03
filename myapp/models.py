from django.db import models

# Create your models here.

class Users(models.Model):
    FullName = models.CharField(max_length=100)
    CardNumber = models.IntegerField()
    inventory = models.IntegerField()
    

    def __str__(self):
        return f"{self.FullName}"

