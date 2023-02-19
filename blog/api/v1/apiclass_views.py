from rest_framework.response import Response
from blog.api.v1.serializers import PostSerializer
from blog.models import Post
from rest_framework.views import APIView 
from django.shortcuts import get_object_or_404
from http import HTTPStatus

""" #APIView class görünümü
class PostDetail(APIView):
    @staticmethod
    def get_post(pk):
        return get_object_or_404(Post, pk=pk)

    def get(self, request, pk, format=None):
        post = self.get_post(pk)
        return Response(PostSerializer(post).data)

    def put(self, request, pk, format=None):
        post = self.get_post(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTPStatus.NO_CONTENT)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_post(pk)
        post.delete()
        return Response(status=HTTPStatus.NO_CONTENT)
"""


#generic view
from rest_framework import mixins
from rest_framework import generics

class PostList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView,):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




