from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "recipe", "created", "updated")
    prepopulated_fields = {"slug": ("title",)}

