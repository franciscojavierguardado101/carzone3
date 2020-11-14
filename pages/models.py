from django.db import models
from django.db import migrations, models
# Create your models here. These are the theme models
#Whenever we want a function inside a class we have to use self
# Also we need to use python manage.py makemigrations and migrate command after that
class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    facebook_link = models.URLField(max_length=100,null=True)
    twitter_link = models.URLField(max_length=100,null=True)
    google_plus_link = models.URLField(max_length=100,null=True)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name
