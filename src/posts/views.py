from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.response import Response


from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, PostCommentSerializer


class PostListCreatApiView(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentListCreateApiView(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    #create comment
    def get_serializer_class(self):
        if 'post_id' in self.kwargs:
            return PostCommentSerializer            #use post_id from url
        return super().get_serializer_class()       #write your own post_id

    #all comments for post
    def get_queryset(self):
        queryset = super().get_queryset()
        if 'post_id' in self.kwargs:
            queryset = queryset.filter(post_id=self.kwargs['post_id'])
        return queryset


class CommentDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class PostUpvote(RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.upvotes += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
