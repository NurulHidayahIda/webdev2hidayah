from django.db import models

# Create your models here.
class Pndftr(models.Model):
    nama = models.CharField(max_length = 50)
    alamat = models.charField(max_length=75)

    def __str__(self):
        return self.nama
