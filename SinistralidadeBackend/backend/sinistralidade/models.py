from django.db import models

# Create your models here.


class distrito(models.Model):
    nome = models.CharField(primary_key=True, max_length=150)


class concelho(models.Model):
    nome = models.CharField(primary_key=True, max_length=150)
    n_distrito = models.CharField(max_length=150)


class utilizador(models.Model):
    cc = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    palavrapasse = models.CharField(max_length=50)
    ocupacao = models.CharField(max_length=50)
    n_distrito = models.CharField(max_length=150)


class acidente(models.Model):
    id = models.AutoField(primary_key=True)
    concelho = models.CharField(max_length=150)
    datahora = models.DateTimeField(auto_now_add=True)
    mortos = models.IntegerField(editable=True)
    feridosg = models.IntegerField(editable=True)
    via = models.CharField(max_length=150)
    km = models.CharField(max_length=150)
    natureza = models.CharField(max_length=150)


class historico (models.Model):
    id = models.AutoField(primary_key=True)
    datahora = models.DateTimeField(auto_now_add=True)
    cc_user = models.IntegerField()
    id_acidente = models.IntegerField()
