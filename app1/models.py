from django.db import models

# Create your models here.
class regi(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    phone=models.IntegerField()
    address=models.TextField()

    

class cp_register(models.Model):
    
    cp_name=models.CharField(max_length=50)
    cp_email=models.EmailField(default=" ")
    cp_password=models.CharField(max_length=50)
    cp_phone = models.CharField(max_length=50) 
    cp_gst_no = models.CharField(max_length=50)

    cp_address=models.TextField(default='')

    def __str__(self):
        return self.cp_name


