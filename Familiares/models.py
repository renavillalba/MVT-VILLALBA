from django.db import models


class Familiar(models.Model):

    nombre = models.CharField(max_length = 50)
    estatura = models.FloatField()
    fecha_de_nacimiento = models.DateField()
