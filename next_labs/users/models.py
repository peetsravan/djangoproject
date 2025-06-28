from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    points_earned= models.IntegerField(default=0)

    def __str__(self):
        return self.username

class Apps(models.Model):
    picture = models.ImageField(upload_to='app_pictures/')
    app_name= models.CharField(max_length=20)
    app_link=models.URLField()
    app_category=models.CharField(max_length=20)
    sub_category=models.CharField(max_length=20)
    description=models.TextField()
    points=models.PositiveIntegerField()

    def __str__(self):
        return self.app_name
    
class task(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    apps=models.ForeignKey(Apps,on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='screenshots/')
    approved= models.BooleanField(default=False)