from django.db import models
from django.utils import timezone
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # publish =  models.DateField(auto_now_add=False, auto_now=False, default=timezone.now)
    publish =  models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)