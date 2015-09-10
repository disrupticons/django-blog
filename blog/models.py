from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	author = models.ForeignKey(User)
	title = models.CharField(max_length=100)
	body = models.TextField()
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	modified_date = models.DateTimeField('date modified', auto_now=True)

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	author = models.ForeignKey(User)
	body = models.TextField()
	parent_post = models.ForeignKey(Post, blank=True, null=True)
	parent_comment = models.ForeignKey("self", blank=True, null=True)
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	modified_date = models.DateTimeField('date modified', auto_now=True)

	def __unicode__(self):
		return ' '.join(self.body.split()[:4]) + '...'