from django.db import models

# Create your models here.
class PG(models.Model):
    sn = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=500)
    rent = models.IntegerField()
    image = models.ImageField(upload_to='static/images/')


    def __str__(self):
        return self.name