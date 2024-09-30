from django.contrib import admin

from .models import Category, Post
from .models import Comment

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)