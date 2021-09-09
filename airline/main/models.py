from django.db import models

# Create your models here.


class Aeroplane(models.Model):
    aeroplane_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    id = models.IntegerField(primary_key=False)

    def __str__(self):
        return self.name
