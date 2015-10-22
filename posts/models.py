from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 50, blank = True)
    body = models.TextField()
    user = models.ForeignKey(User, blank = True)
    ref = models.ForeignKey('self', blank = True)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    