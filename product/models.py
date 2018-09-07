from django.db import models
from datetime import datetime

class Product(models.Model):
  thumbnail = models.ImageField(upload_to='images/')
  title = models.CharField(max_length=50)
  caption = models.CharField(max_length=200)
  pub_date = models.DateTimeField(default=datetime.now)
  image = models.ImageField(upload_to='images/')
  spec = models.TextField(default='SOME STRING')