from django.db import models
from django.contrib.auth.models import AbstractUser

# Foydalanuvchi modeli
class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.username

# Sayohat modeli
class Trip(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='trips')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    friends = models.ManyToManyField(CustomUser, related_name='shared_trips', blank=True)

    def __str__(self):
        return self.name
