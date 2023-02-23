from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from blog.api.v1 import api_views
from blog.api.v1 import apiclass_views
from blog.api.v1 import views as aviews
from rest_framework.authtoken import views




urlpatterns = [
    path("posts/", api_views.post_list, name="api_post_list"),
    path("posts/<int:pk>", api_views.post_detail, name="api_post_detail"),
    #path("postlars/<int:pk>", apiclass_views.PostDetail.as_view()),      #apiclass view için

    #path("postlar/", apiclass_views.PostList.as_view()),                   #generic mixin için
    #path("postlar/<int:pk>", apiclass_views.PostDetail.as_view()),         #generic mixin için 

    path("postlar/", aviews.PostList.as_view()),                   #generic için
    path("postlar/<int:pk>", aviews.PostDetail.as_view()),         #generic için 
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token),

]

urlpatterns = format_suffix_patterns(urlpatterns)




# requests.get("http://127.0.0.1:8000/api/v1/posts/", headers={"Authorization": "e205bdd823797df036e32e9d913b197f7538d6ae"})
# requests.get("http://127.0.0.1:8000/api/v1/postlar",auth=HTTPBasicAuth("root", "1a")) 

# token e205bdd823797df036e32e9d913b197f7538d6ae