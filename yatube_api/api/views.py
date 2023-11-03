from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from posts.models import Group, Post
from .serializers import GroupSerializer, PostSerializer, CommentSerializer
# Create your views here.


class PermissionsMixin:
    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied("Менять чужой контент запрещено")
        super().perform_update(serializer)

    def perform_destroy(self, serializer):
        if serializer.author != self.request.user:
            raise PermissionDenied("Удалять чужой контент запрещено")
        super().perform_destroy(serializer)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(PermissionsMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(PermissionsMixin, viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return self.get_post().comments.all()

    def get_post(self):
        post_id = self.kwargs.get('id')
        return get_object_or_404(Post, pk=post_id)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())
