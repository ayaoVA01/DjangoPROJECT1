from django.contrib import admin
from app.models import CustomUser
# Register your models here.


class Custom_admin(admin.ModelAdmin):
    list_display=['username','email','user_type', 'profile_picture']
admin.site.register(CustomUser,Custom_admin)

