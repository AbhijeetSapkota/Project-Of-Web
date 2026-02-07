from django.contrib import admin
from mainapp.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'user', 'is_anonymous', 'created_at')
    list_filter = ('category', 'is_anonymous', 'created_at')
    search_fields = ('title', 'description', 'user__username')
