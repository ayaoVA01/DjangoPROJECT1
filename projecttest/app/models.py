
from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        (1,'hod'),
        (2,'ative'))
    user_type = models.CharField(choices =  USER,default = 1,max_length = 50)
    profile_picture = models.ImageField(upload_to = 'media/profileImage',blank = True,null = True)
    
    phone_number = models.CharField(max_length = 15)
    age = models.CharField('age', max_length = 3)
    date = models.CharField(max_length = 30)
    def show_img(self):
        if self.profile_picture:
            return format_html('<img src="%s" height ="50px">' % self.profile_picture.url)
        return 'NULL'
    show_img.allow_tags=True
   
    
    
      
