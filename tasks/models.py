from django.db import models

# Create your models here.

class Task(models.Model):
    budget_edit = models.TextField(blank=True)
    budget = models.TextField(blank=True)
    payment = models.TextField(blank=True)
    title = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)