from django.contrib import admin
from .models import Historiaclinica
from django.contrib.auth.models import Permission
# Register your models here.
admin.site.register(Historiaclinica)
admin.site.register(Permission)