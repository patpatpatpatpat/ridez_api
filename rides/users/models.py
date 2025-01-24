import uuid
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from .constants import RideStatus, Role


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=10, choices=Role.choices)

    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Ride(AbstractBaseModel):
    status = models.CharField(max_length=15, choices=RideStatus.choices)
    rider = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ridden_rides")
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="driven_rides")
    pickup_latitude = models.DecimalField(max_digits=12, decimal_places=8, null=True, blank=True)
    pickup_longitude = models.DecimalField(max_digits=13, decimal_places=8, null=True, blank=True)
    dropoff_latitude = models.DecimalField(max_digits=12, decimal_places=8, null=True, blank=True)
    dropoff_longitude = models.DecimalField(max_digits=13, decimal_places=8, null=True, blank=True)
    pickup_time = models.DateTimeField(null=True, blank=True)


class RideEvent(AbstractBaseModel):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    description = models.TextField()
