from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'v1/posts', PostViewSet)
router.register(r'v1/groups', GroupViewSet)
router.register(r'v1/posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')


urlpatterns = [

    path('v1/api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),

]