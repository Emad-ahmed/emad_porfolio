from django.contrib import admin
from emadapp.models import Conatct
# Register your models here.


@admin.register(Conatct)
class ConatctAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'dateemail']
