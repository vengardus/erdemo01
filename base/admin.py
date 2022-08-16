from django.contrib import admin

# Register your models here.

from .models import User, License, UnidadMedida, Empleado, Producto
from .models import CaInvCab, Stock

admin.site.register(User)
admin.site.register(License)
admin.site.register(UnidadMedida)
admin.site.register(Empleado)
admin.site.register(Producto)
admin.site.register(CaInvCab)
admin.site.register(Stock)