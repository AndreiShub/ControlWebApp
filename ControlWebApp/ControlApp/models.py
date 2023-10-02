from django.db import models
from datetime import date

class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    date_posted = models.DateField(default=date.today)
    
