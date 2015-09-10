from django.contrib import admin

from .models import Post, Comment

class CommentInline(admin.StackedInline):
	model = Comment
	extra = 2

class PostAdmin(admin.ModelAdmin):
	inlines = [CommentInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
