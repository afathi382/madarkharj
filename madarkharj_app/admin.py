from django.contrib import admin

from .models import Profile, Group, Factor, Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Group)
admin.site.register(Factor)
admin.site.register(Comment)
