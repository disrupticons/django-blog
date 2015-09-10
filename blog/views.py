from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.core.urlresolvers import reverse
from django.http import Http404

from django.contrib.auth.decorators import login_required

from .models import Post, Comment

class IndexView(generic.ListView):
	template_name = 'blog/index.html'
	context_object_name = 'latest_blog_posts'

	def get_queryset(self):
		return Post.objects.order_by('-pub_date')

class PostView(generic.DetailView):
	model = Post
	template_name = 'blog/post.html'

@login_required
def addPost(request):
	print(request.user);
	if(request.method == 'GET'):
		# render form
		return render(request, 'blog/new_post.html')
	elif(request.method == 'POST'):
		# save new post
		Post.objects.create(author=request.user, title=request.POST['title'], body=request.POST['body'])
		return redirect(reverse('blog:index'))
	else:
		raise Http404()

@login_required
def modifyPost(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	checkAuthor(request, post)
	if(request.method == 'GET'):
		# render form
		return render(request, 'blog/new_post.html', {
			'post' : post,
		})
	elif(request.method == 'POST'):
		# update post
		post.body = request.POST['body']
		post.save()
		return redirect(reverse('blog:post', args=(post_id,)))
	else:
		raise Http404()

@login_required
def deletePost(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	checkAuthor(request, post)
	post.delete()
	return redirect(reverse('blog:index'))

@login_required
def addComment(request, post_id=None, comment_id=None):
	next = getNextURL(request)
	if(request.method != 'POST'):
		raise Http404();
	if(post_id):
		# add comment to post
		post = get_object_or_404(Post, pk=post_id)
		Comment.objects.create(author=request.user, body=request.POST['body'], parent_post=post)
	elif(comment_id):
		# add reply to comment
		comment = get_object_or_404(Comment, pk=comment_id)
		Comment.objects.create(author=request.user, body=request.POST['body'], parent_comment=comment)
	return redirect(next)

@login_required
def modifyComment(request, comment_id):
	next = getNextURL(request)
	comment = get_object_or_404(Comment, pk=comment_id)
	checkAuthor(request, comment)
	comment.body = request.POST['body']
	comment.save()
	return redirect(next)

@login_required
def deleteComment(request, comment_id):
	next = getNextURL(request)
	comment = get_object_or_404(Comment, pk=comment_id)
	checkAuthor(request, comment)
	comment.delete()
	return redirect(next)

def checkAuthor(request, obj):
	''' Checks if the given post/comment was authored by the logged in user '''
	if(request.user.id != obj.author.id):
		raise Http404('You are not authorized to perform this action')

def getNextURL(request):
	''' Gets the url specified by 'next' GET parameter; uses default otherwise '''
	try:
		next = request.GET['next']
	except KeyError:
		return reverse('blog:index')
	return next;