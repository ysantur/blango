from rest_framework import generics
from blog.api.v1.serializers import PostSerializer, UserSerializer, PostDetailSerializer
from blog.models import Post
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser
from blog.api.v1.permissions import AuthorModifyOrReadOnly, deneme
from django.contrib.auth.models import User

class PostList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication]
    #permission_classes = [IsAdminUser]
    #permission_classes = [AuthorModifyOrReadOnly]

    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
