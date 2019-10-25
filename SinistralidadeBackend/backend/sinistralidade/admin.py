from django.contrib import admin
from django.db import models
from .models import utilizador, distrito, concelho, acidente


admin.site.register(distrito)
admin.site.register(utilizador)
admin.site.register(concelho)
admin.site.register(acidente)

# Register your models here.
