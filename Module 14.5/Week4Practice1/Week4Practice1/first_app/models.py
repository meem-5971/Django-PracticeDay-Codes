from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    roll = models.AutoField(primary_key=True)
    registrant_id = models.BigIntegerField()
    passed= models.BooleanField()
    min_age = models.SmallIntegerField()
    max_fees = models.BigIntegerField()
    goals = models.TextField()

    def __str__(self):
        return f"Name:{self.name}"