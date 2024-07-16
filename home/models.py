from django.db import models
from datetime import datetime
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    desc = models.TextField(max_length=50)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
