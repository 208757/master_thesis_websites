from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class ServiceProvider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=20)


class Subscriber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Authentication(models.Model):
    user = models.ForeignKey(Subscriber, related_name='authentication', on_delete=models.CASCADE)
    service = models.ForeignKey(ServiceProvider, related_name='authentication', on_delete=models.CASCADE)
    process_id = models.IntegerField(default=0)
    content = models.CharField(max_length=256)
    state = models.CharField(max_length=20)


class Subscription(models.Model):
    subscriber = models.ForeignKey(Subscriber, related_name='subscribers', on_delete=models.CASCADE, default=None)
    service = models.ForeignKey(ServiceProvider, related_name='subscriptions', on_delete=models.CASCADE, default=None)
