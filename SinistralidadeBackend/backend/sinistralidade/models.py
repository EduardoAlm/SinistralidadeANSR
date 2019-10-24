from django.db import models

# Create your models here.


class utilizador(models.Model):
    cc = models.IntegerField(primary_key=True, editable=True)
    nome = models.CharField(max_length=50)
    palavrapasse = models.CharField(max_length=50)
    ocupacao = models.CharField(max_length=50)
    n_distrito = models.CharField(max_length=150)
