
from django.db import models
from django.contrib.auth.models import User
 
 
class Customer(models.Model):
 
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
 
    phone = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    profile_photo = models.ImageField(upload_to='customers/', null=True, blank=True)
 
    created_at = models.DateTimeField(auto_now_add=True, null=True)
 
    def __str__(self):
        return self.user.username