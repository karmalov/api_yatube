from rest_framework import serializers

from posts.models import Post, Group, Comment


class PostBase(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        fields = '__all__'


class PostSerializer(PostBase):

    class Meta(PostBase.Meta):
        model = Post


class CommentSerializer(PostBase):

    class Meta(PostBase.Meta):
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
