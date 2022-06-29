from django.contrib import admin
from emadapp.models import Conatct, Blog
# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'description',  'dateblog']


@admin.register(Conatct)
class ConatctAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'dateemail']
