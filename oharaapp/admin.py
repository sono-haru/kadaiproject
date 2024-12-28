from django.contrib import admin
from .models import Tokuten_post

class User_post(admin.ModelAdmin):
    list_display=('id','subject','num')
    list_display_links=('id','subject','num')
admin.site.register(Tokuten_post,User_post)
