from django.db import models
from django.utils.timezone import now

# Create your models here.
class Monitor(models.Model):
  title = models.CharField(max_length=200)
  link = models.CharField(max_length=200, primary_key=True)
  created_at = models.DateTimeField(default=now)