from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    blog_imaGE = models.ImageField(upload_to='images/blog/')
    dateblog = models.DateTimeField(auto_now_add=True)


class Conatct(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    dateemail = models.DateTimeField(auto_now_add=True)
