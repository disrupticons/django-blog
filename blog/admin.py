from django.contrib import admin

from .models import Post, Comment, PostComment, Reply

# class CommentInline(admin.StackedInline):
# 	model = Comment
# 	extra = 2

# class PostAdmin(admin.ModelAdmin):
# 	inlines = [CommentInline]

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(PostComment)

