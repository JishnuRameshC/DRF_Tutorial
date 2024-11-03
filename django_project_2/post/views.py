from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics,viewsets
from rest_framework.permissions import IsAdminUser

from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer,UserSerializer
from .models import Post
# Create your views here.



class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# class PostListView(generics.ListCreateAPIView):
#     permission_classes = (IsOwnerOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsOwnerOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


# class UserListView(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAdminUser]
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

# class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.IsAdminUser]
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer