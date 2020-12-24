from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListCreatApiView.as_view(), name='post_list'),
    path('posts/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('comments/', views.CommentListCreateApiView.as_view(), name='comment_list'),
    path('comments/<int:pk>', views.CommentDetailView.as_view(), name='comment_detail'),
    path('posts/<int:pk>/upvote', views.PostUpvote.as_view(), name='votes'),
]