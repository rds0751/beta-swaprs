from django.db import models
from django.contrib.auth.models import User

class UserLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=100,blank=True)

    class Meta:
        ordering = ['-id']

class SystemLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    type = models.CharField(max_length=100,blank=True)
    create_date = models.DateTimeField(auto_now_add=True)



