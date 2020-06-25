from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """ Posts """
    title = models.CharField(max_length=150)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=26)
    upvote = models.ManyToManyField(User, related_name="users_upvotes")


class Comment(models.Model):
    """ Comments """
    author = models.CharField(max_length=150)
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="children",
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
