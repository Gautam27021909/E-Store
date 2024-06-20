from django.db import models

class Register(models.Model):
    fname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    pno   = models.IntegerField(default='')
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)