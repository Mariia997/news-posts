from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListCreatApiView.as_view(), name='post-list'),
    path('posts/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('comments/', views.CommentListCreateApiView.as_view(), name='comment-list'),
    path('comments/<int:pk>', views.CommentDetailView.as_view(), name='comment-detail'),
    path('posts/<int:pk>/upvotes', views.PostUpvote.as_view(), name='votes'),
    path('posts/<int:post_id>/comments', views.CommentListCreateApiView.as_view(), name='post-comments'),
]