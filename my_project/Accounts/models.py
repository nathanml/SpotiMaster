from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    Genre_Choices = [
        ('KnvZfZ7vAvd', 'Blues'),
        ('KnvZfZ7vAeJ', 'Classical'),
        ('KnvZfZ7vAv6', 'Country'),
        ('KnvZfZ7vAv1', 'Hip-Hop / Rap'),
        ('KnvZfZ7vAvE', 'Jazz'),
        ('KnvZfZ7vAev', 'Pop'),
        ('KnvZfZ7vAee', 'R&B'),
        ('KnvZfZ7vAeA', 'Rock'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, default='')
    spotify_username = models.CharField(max_length=100, default='')
    genre = models.CharField(
        max_length=25, 
        choices = Genre_Choices,
        default='')
    
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)