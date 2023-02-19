from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from blog.api.v1 import api_views
from blog.api.v1 import apiclass_views
from blog.api.v1 import views



urlpatterns = [
    path("posts/", api_views.post_list, name="api_post_list"),
    path("posts/<int:pk>", api_views.post_detail, name="api_post_detail"),
    #path("postlars/<int:pk>", apiclass_views.PostDetail.as_view()),      #apiclass view için

    #path("postlar/", apiclass_views.PostList.as_view()),                   #generic mixin için
    #path("postlar/<int:pk>", apiclass_views.PostDetail.as_view()),         #generic mixin için 

    path("postlar/", views.PostList.as_view()),                   #generic için
    path("postlar/<int:pk>", views.PostDetail.as_view()),         #generic için 

]

urlpatterns = format_suffix_patterns(urlpatterns)




