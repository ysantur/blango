from rest_framework import generics, viewsets
from blog.api.v1.serializers import PostSerializer, UserSerializer, PostDetailSerializer,TagSerializer
from blog.models import Post, Comment, Tag
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser
from blog.api.v1.permissions import AuthorModifyOrReadOnly, deneme
from django.contrib.auth.models import User
from rest_framework.decorators import action



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


from rest_framework.response import Response

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    @action(methods=["get"], detail=True, name="Posts with the Tag")
    def posts(self, request, pk=None):
        tag = self.get_object()
        post_serializer = PostSerializer(tag.posts, many=True, context={"request": request})
        return Response(post_serializer.data)


