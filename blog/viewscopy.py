from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.core.urlresolvers import reverse
from django.http import Http404

from .models import Post, Comment

class IndexView(generic.ListView):
	template_name = 'blog/index.html'
	context_object_name = 'latest_blog_posts'

	def get_queryset(self):
		return Post.objects.order_by('-pub_date')

class PostView(generic.DetailView):
	model = Post
	template_name = 'blog/post.html'

def addPost(request):
	if(request.method == 'GET'):
		return render(request, 'blog/new_post.html', {
			# 'action' : reverse('blog:addPost')
		})
	elif(request.method == 'POST'):
		Post.objects.create(author=request.user, title=request.POST['title'], body=request.POST['body'])
		return redirect(reverse('blog:index'))
	else:
		raise Http404()

def modifyPost(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	print(reverse('blog:index'))
	if(request.method == 'GET'):
		return render(request, 'blog/new_post.html', {
			'post' : post,
			'action' : reverse('blog:modifyPost', args=(post_id,))
		})
	elif(request.method == 'POST'):
		checkAuthor(request, post)
		post.body = request.POST['body']
		post.save()
		return redirect(reverse('blog:post', args=(post_id,)))
	else:
		raise Http404()
	
	

def deletePost(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	checkAuthor(request, post)
	post.delete()
	return redirect(reverse('blog:index'))

def addComment(request, post_id, comment_id):
	next = getNextURL()
	if(post_id):
		post = get_object_or_404(Post, pk=post_id)
		Comment.objects.create(author=request.user, body=request.POST['body'], parent_post=post)
	elif(comment_id):
		comment = get_object_or_404(Comment, comment_id)
		Comment.objects.create(author=request.user, body=request.POST['body'], parent_comment=comment)
	return redirect(next)

def modifyComment(request, comment_id):
	next = getNextURL()
	comment = get_object_or_404(Comment, pk=comment_id)
	checkAuthor(request, comment)
	comment.body = request.POST['body']
	comment.save()
	return redirect(next)

def deleteComment(request, comment_id):
	next = getNextURL()
	comment = get_object_or_404(Comment, pk=comment_id)
	checkAuthor(request, comment)
	comment.delete()
	return redirect(next)

def checkAuthor(request, obj):
	if(request.user.id != obj.author.id):
		raise Http404('You are not authorized to perform this action')

def getNextURL():
	try:
		next = request.GET['next']
	except KeyError:
		return reverse('blog:index')
	return next;