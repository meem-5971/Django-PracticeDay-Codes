from django.db import models
from musician.models import Musician

# Create your models here.
rating=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')]
class Album(models.Model):
    album_name=models.CharField(max_length=50)
    musician=models.ForeignKey(Musician,on_delete=models.CASCADE)
    release_date=models.DateField(auto_now_add=True)
    rating=models.CharField(max_length=2, choices=rating)

    def __str__(self):
        return self.album_name
