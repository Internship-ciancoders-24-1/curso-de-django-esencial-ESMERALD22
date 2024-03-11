"""Posts URLs."""

# Django
from django.urls import path

# Views
from posts import views

#    path('',posts_views.list_posts, name ='feed'),
#   path('posts/new',posts_views.create_post, name ='create_post'),

urlpatterns = [

    path(
        route='',
        view=views.PostsFeedView.as_view(),
        name='feed'
    ),

    path(
        route='posts/new/',
        view=views.CreatePostView.as_view(),
        name='create_post'
    ),
    path(
        route='posts/<int:pk>/',
        view=views.PostDetailView.as_view(),
        name='detail'
    )
]