# from django.urls import path
# from .views import PostListView, PostDetailView, UserListView, UserDetailView   

# urlpatterns = [
#     path('',PostListView.as_view(), name='post_list'),
#     path('<int:pk>',PostDetailView.as_view(), name='post_detail'),
#     path('users/',UserListView.as_view(), name='user_list'),
#     path('users/<int:pk>',UserDetailView.as_view(), name='user_detail'),
# ]

from .views import PostViewSet, UserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('users', UserViewSet)

urlpatterns = router.urls