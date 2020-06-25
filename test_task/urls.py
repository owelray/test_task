from django.urls import path
from .views import (
    PostListView,
    PostRetrieveView,
    PostUpvoteView,
    CommentCreateView,
    CommentRetrieveView,
    CommentListView,
)

urlpatterns = [
    path("posts/", PostListView.as_view()),
    path("posts/<int:pk>/", PostRetrieveView.as_view()),
    path("posts/<int:pk>/upvote/", PostUpvoteView.as_view()),
    path("posts/comments/", CommentListView.as_view()),
    path("posts/comments/add/", CommentCreateView.as_view()),
    path("posts/comments/<int:pk>/", CommentRetrieveView.as_view()),
]
