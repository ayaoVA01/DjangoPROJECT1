




from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import User



# Create your models here.

class Chat(models.Model):
    # user_chat =models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=60)
    pic=models.ImageField(upload_to='media',blank=True, null=True)
    friends = models.ManyToManyField('Friend', related_name = 'myfriends')
    
    class Meta:
        verbose_name_plural= 'ແຊດ'
    def __str__(self):
        return self.name

class Friend(models.Model):
    profile = models.OneToOneField(Chat, on_delete =models.CASCADE)
    
    class Meta:
        verbose_name_plural= 'ຫມູ່'
    def __str__(self):
        return self.profile.name




class Status(models.Model):
    title_status=models.CharField(max_length=60)
    dsp_status= models.TextField()
    date_status=models.DateTimeField(auto_now_add=True)
    image_status=models.ImageField(upload_to='media')
    update_status=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural= 'ສະຖານະ'
    def show_image_status(self):
        if self.image_status:
            return format_html('<img src="%s" height ="50px">' % self.image_status.url)
        return 'NULL'
    show_image_status.allow_tags=True


class Post(models.Model):
    # post_user =models.OneToOneField(User,on_delete=models.CASCADE)
    time_post = models.TimeField(auto_now_add = True)
    dsp_post= models.TextField()
    date_post=models.DateTimeField(auto_now_add=True)
    image_post=models.ImageField(upload_to='media')
    like_post = models.IntegerField()
    

    class Meta:
        verbose_name_plural= 'ໂພສ'

    def show_image_profile(self):
        if self.image_post:
            return format_html('<img src="%s" height ="50px">' % self.image_post.url)
        return 'NULL'
    show_image_profile.allow_tags=True
   


