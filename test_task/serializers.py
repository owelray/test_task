from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    """ Showing a post fields from a tuple """

    upvotes = serializers.IntegerField(
        source="upvote.count", read_only=True
    )  # counting upvotes

    class Meta:
        model = Post
        fields = ("title", "link", "created_at", "upvotes", "author")


class CommentSerializer(serializers.ModelSerializer):
    """ Showing a comment fields from a tuple """

    class Meta:
        model = Comment
        fields = ("author", "content", "created_at")


class PostRetrieveSerializer(serializers.ModelSerializer):
    """ Showing a post field from a tuple of the given post """

    upvotes = serializers.IntegerField(source="upvote.count", read_only=True)
    comments = CommentSerializer(many=True)  # inserts a comments into the given post

    class Meta:
        model = Post
        fields = ("title", "link", "created_at", "upvotes", "author", "comments")


class CommentCreateSerializer(serializers.ModelSerializer):
    """ Creates a comment """

    class Meta:
        model = Comment
        fields = "__all__"
