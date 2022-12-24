from django.urls import path
from . import views
urlpatterns = [
    path('', views.PostView.as_view()),
    path("<int:pk>/", views.PostDetail.as_view()),
    path("review/<int:pk>/", views.AddComments.as_view(), name="add_comments"),

    path("example/", views.Example.as_view()),
    path("example/<slug:slug>/", views.Example_Detail.as_view(), name="example_slug")
]