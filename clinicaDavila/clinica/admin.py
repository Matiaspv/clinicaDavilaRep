from django.contrib import admin

# Register your models here.


from . models import Doctor, Especialidad

admin.site.register(Doctor)
admin.site.register(Especialidad)