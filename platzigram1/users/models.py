
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    """Proxy model that extends the base data with otje information."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website= models.URLField(max_length=255, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.TextField(max_length=20, blank=True)
    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
