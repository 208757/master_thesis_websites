from django.contrib import admin
from .models import User, ServiceProvider, Authentication, Subscriber, Subscription


# Register your models here.
admin.site.register(ServiceProvider)
admin.site.register(Authentication)
admin.site.register(Subscriber)
admin.site.register(Subscription)