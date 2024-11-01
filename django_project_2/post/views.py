from django.shortcuts import render
from rest_framework import generics,permissions

from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer
from .models import Post
# Create your views here.


class PostListView(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer