from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Operation(models.Model):
    user = models.ForeignKey(User, related_name='operations', on_delete=models.CASCADE)
    state = models.CharField(max_length=20)
    operation_type = models.CharField(max_length=20)
    operation_number = models.IntegerField()