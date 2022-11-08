
from django.contrib import admin
from chat_app.models import Status,Chat,Post,Friend

# Register your models here.

admin.site.register([Chat,Friend])

class Status_admin(admin.ModelAdmin):
    list_display=['title_status','date_status','update_status','show_image_status']
    search_fields=['title_status']
    list_filter=['title_status']
admin.site.register(Status,Status_admin)


class Post_admin(admin.ModelAdmin):
    list_display=['date_post','show_image_profile']
    search_fields=['title_profile']
admin.site.register(Post,Post_admin)



