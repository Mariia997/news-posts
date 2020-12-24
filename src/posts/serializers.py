from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "content", "creation_date", "upvotes", "author_name", "link")
        extra_kwargs = {
            'upvotes': {'read_only': True},
            'creation_date': {'read_only': True}
        }


class CommentSerializer(serializers.ModelSerializer):
    post_id = serializers.IntegerField(source="post.id")

    class Meta:
        model = Comment
        fields = ("id", "author_name", "content", "creation_date", "post_id")
        extra_kwargs = {
            'creation_date': {'read_only': True}
        }
