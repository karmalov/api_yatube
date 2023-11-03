from rest_framework import serializers

from posts.models import Post, Group, Comment


class AuthorMixin:
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)


class PostSerializer(AuthorMixin, serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(AuthorMixin, serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
