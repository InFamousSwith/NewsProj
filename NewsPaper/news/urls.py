from django.urls import path
from .views import PostList, PostDetail, PostCreateView, PostSearch, PostDetailView, PostUpdateView, PostDeleteView# импортируем наше представление

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', PostSearch.as_view()),
    path('add/', PostCreateView.as_view(), name='post_create'),  # Ссылка на создание товара
    path('<int:pk>/edit', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
]