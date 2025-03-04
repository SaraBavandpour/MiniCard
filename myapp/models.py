from django.db import models

# Create your models here.

class Users(models.Model):
    FullName = models.CharField(max_length=100)
    CardNumber = models.IntegerField(primary_key=True)
    inventory = models.IntegerField()
    amount = models.IntegerField(null=True)
    

    def __str__(self):
        return f"{self.FullName}"

