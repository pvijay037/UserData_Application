from django.db import models

# Create your models here.
from django.db import models

class UserData(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    dob = models.DateField()

    def __str__(self):
        return self.name