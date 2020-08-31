from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    LikeView,
    CategoryPostView,
    CategoryCreateView,
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<slug>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<slug>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('category/new/', CategoryCreateView.as_view(), name='category-create'),
    path('category/<slug>/', CategoryPostView.as_view(), name='category-posts'),
    path('about/', views.about, name='blog-about'),
    path('like/<int:pk>', LikeView, name="like-post")
] 