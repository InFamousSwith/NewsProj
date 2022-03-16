from django.urls import path
from .views import PostList, PostDetail, PostCreateView # импортируем наше представление

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('search/', PostList.as_view()),
    path('create/', PostCreateView.as_view(), name='post_create'),  # Ссылка на создание товара
]