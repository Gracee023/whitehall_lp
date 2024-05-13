from django.db import models

# Create your models here.
class Blog(models.Model):

    name = models.TextField(max_length=100)
    content = models.TextField(max_length=1000)
