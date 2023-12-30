from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'owner', 'post', 'created_at')  # Add 'post' here
    list_filter = ('created_at', 'owner')
    search_fields = ('content',)

admin.site.register(Comment, CommentAdmin)