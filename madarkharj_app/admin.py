from django.contrib import admin

from .models import Profile, Group, Group_Profiles, Factor, Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Group)
admin.site.register(Group_Profiles)
admin.site.register(Factor)
admin.site.register(Comment)
