from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout
from django.views.generic.base import View
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    ListCreateAPIView,
)
from .serializers import PostSerializer, PostRetrieveSerializer, \
    CommentCreateSerializer
from .models import Post, Comment


class PostListView(ListCreateAPIView):
    """ Displays a list of posts ordered by newest """
    queryset = Post.objects.all().order_by("-id")
    serializer_class = PostSerializer


class PostRetrieveView(RetrieveUpdateDestroyAPIView):
    """ Shows a given post, can also delete and update it """
    queryset = Post.objects.all()
    serializer_class = PostRetrieveSerializer


class PostUpvoteView(APIView):
    """ Upvoting a given post, works only with logged users """
    def post(self, request, pk):
        post_item = Post.objects.get(id=pk)
        user_ups = User.objects.filter(users_upvotes=pk)
        current_user = request.user
        if request.user.is_authenticated:
            if current_user not in user_ups:
                post_item.upvote.add(current_user)
                post_item.save()
                return Response(status=201)
            else:
                post_item.upvote.remove(current_user)
                post_item.save()
                return Response(status=201)
        else:
            return HttpResponseRedirect("/login")


class CommentCreateView(CreateAPIView):
    """ Creates a comment inherited from post """
    serializer_class = CommentCreateSerializer


class CommentRetrieveView(RetrieveUpdateDestroyAPIView):
    """ Shows a given comment, can also delete and update it """
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer


class CommentListView(ListAPIView):
    """ Displays a list of comments ordered by newest """
    queryset = Comment.objects.all().order_by("-id")
    serializer_class = CommentCreateSerializer


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/api/posts"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        redirect_to = request.GET.get("next", "")
        logout(request)
        return HttpResponseRedirect(redirect_to)
