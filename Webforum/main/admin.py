from django.contrib import admin
from .models import Post, User, Theme


admin.site.register(Post)
admin.site.register(Theme)
admin.site.register(User)
