from django.db import models

# Create your models here.

class Snow (models.Model):

    #wartość początkowa bez śniegu 
    input_before_snow = models.CharField(max_length=400)

    #wartość po opadzie śniegu 
    output_after_snow = models.CharField(max_length=400)

    def __str__(self):
        return self.input_before_snow
