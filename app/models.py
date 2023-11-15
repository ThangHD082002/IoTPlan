from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=254)
    age = models.IntegerField()


class Data(models.Model):
    temperature = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.temperature)
