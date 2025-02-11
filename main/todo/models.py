from django.db import models

# Create your models here.
class Task(models.Model):
    unique_id=models.AutoField(primary_key=True, unique=True)
    task=models.CharField(max_length=100)