from django.db import models

# Create your models here.
class User(models.Model):
    nr_cc = models.IntegerField(primary_key=True, editable=True)
    username = models.TextField(max_length=50)
    email = models.TextField(max_length=50)
    distrito = models.TextField(max_length=150)
