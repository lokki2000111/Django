from django.urls import path, include

from media_app.api.views.media import MediaViewSet
from tags_app.api.views.tags import TagsViewSet
from . import views
from .api.views.publications import PostsViewSet, PostForTagView, PostLikeView
from .api.views.router import api_router
from .views import LoginUser, Profile, ProfileUpdate, BaseTemplate, LogoutView, Tags, GetTag, PostListView


urlpatterns = [
    path('api/', include(api_router.urls)),
    path('api/posts_with_tag/<str:tag>/', PostForTagView.as_view(), name='api-posts'),
    path('api/posts_with_like/<int:id>/', PostLikeView.as_view(), name='api-postslike'),
    path('api/tags/', TagsViewSet.as_view(), name='api-tags'),
]
