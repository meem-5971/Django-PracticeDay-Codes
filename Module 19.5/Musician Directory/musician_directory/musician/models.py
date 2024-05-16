from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=12)
    instrumentation = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
