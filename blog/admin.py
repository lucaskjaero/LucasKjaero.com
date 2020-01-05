from django.contrib import admin

from .models import Category, Post

admin.site.register(Category)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'category', 'published')


admin.site.register(Post, PostAdmin)
