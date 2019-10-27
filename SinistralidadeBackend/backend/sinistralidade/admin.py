from django.contrib import admin
from django.db import models
from .models import utilizador, distrito, concelho, acidente, historico


admin.site.register(distrito)
admin.site.register(utilizador)
admin.site.register(concelho)
admin.site.register(acidente)
admin.site.register(historico)

# Register your models here.
