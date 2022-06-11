from django.db import models

# Create your models here.


class Conatct(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    dateemail = models.DateTimeField(auto_now_add=True)
