from django.urls import path
from . import views
urlpatterns = [
    path('', views.PostView.as_view()),
    path("<slug:slug>/", views.PostDetail.as_view(), name="current_post"),
    path("review/<int:pk>/", views.AddComments.as_view(), name="add_comments"),
    path("addpage/", views.AddPost.as_view(), name="add_post"),


    path("example/", views.Example.as_view()),
    path("example/<slug:slug>/", views.Example_Detail.as_view(), name="example_slug"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("register/", views.RegisterUser.as_view(), name="register"),
    path("logout/", views.logout_user, name="logout"),

]