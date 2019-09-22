from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),  # class based view
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),  # class based userPostList view
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # class based detail view
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # class based create view
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),  # class based update view
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),  # class based delete view
    # path('', views.home, name='blog-home'), # function based view
    path('about/', views.about, name='blog-about')
]
