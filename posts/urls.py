from django.urls import path
from .views import PostView, post_upload, like_post, registration, signin, signout,index

urlpatterns = [
    path("userpost", PostView.as_view(), name="userpost"),
    path("upload", post_upload, name="upload"),
    path("likes", like_post, name="like_post"),
    path("accounts/signup", registration, name="registration"),
    path("accounts/signin", signin, name="signin"),
    path("signout", signout, name="signout"),
    path("home",index,name="home")
]
