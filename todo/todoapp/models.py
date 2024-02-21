from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TaskList(models.Model):
    title=models.CharField(max_length=50)
    detail=models.CharField(max_length=500)
    due_dt=models.DateField()
    is_completed=models.BooleanField(default=0)
    is_activate=models.BooleanField(default=1)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,db_column="user_id")