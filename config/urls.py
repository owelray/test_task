from django.contrib import admin
from django.urls import path, include
from test_task.views import LogoutView, LoginFormView, RegisterFormView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", LoginFormView.as_view()),
    path("register/", RegisterFormView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("api/", include("test_task.urls")),
]
