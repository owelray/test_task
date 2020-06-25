from celery import app
from .models import Post


@app.shared_task()
def upvotes_reset():
    for post in Post.objects.all():
        post.upvote.clear()
