from django.contrib import admin
from main.models import *


# Register your models here.


class MediaPostAdmin(admin.ModelAdmin):
	list_display = ['time', 'username']


admin.register(Media)
admin.site.register(Media, MediaPostAdmin)

# class BlogPostAdmin(admin.ModelAdmin):
#     list_display = ['title', 'body', 'timestamp']


# admin.register(BlogPost, BlogPostAdmin)
# admin.site.register(BlogPost, BlogPostAdmin)

# admin.site.register(DiaryPost, BlogPostAdmin)
