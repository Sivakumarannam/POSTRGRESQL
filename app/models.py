from django.db import models

# Create your models here.
class Movies(models.Model):
    titlename=models.CharField(max_length=100)
    directorname=models.CharField(max_length=100)
    year=models.IntegerField()
    def __str__(self):
        return self.titlename


class Actors(models.Model):
    titlename=models.ForeignKey(Movies,on_delete=models.CASCADE)
    heroname=models.CharField(max_length=100)
    heroinename=models.CharField(max_length=100)
    def __str__(self):
        return self.heroname

    

