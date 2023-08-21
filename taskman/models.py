from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import get_user_model
import datetime
# from django.contrib.auth.models import User

User = get_user_model()

# Create your models here.
class todo(models.Model):
    status_choice = [
        ('pending','pending'),
        ('completed','completed')
    ]

    title = models.CharField(max_length=50)
    status = models.CharField(max_length=20,choices=status_choice)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)


class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)
    object_details = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

