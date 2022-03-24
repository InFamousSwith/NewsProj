from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from datetime import datetime
from .filters import PostFilter
from .forms import PostForm



class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = ['-id']
    paginate_by = 10
    form_class = PostForm


class PostSearch(ListView):
    model = Post
    template_name = "news/search.html"
    context_object_name = 'news'
    ordering = ['-id']
    form_class = PostForm
    paginate_by = 10

    # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET,
                                       queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        # отправляем пользователя обратно на GET-запрос.
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        return PostFilter(self.request.GET, queryset=queryset).qs


# создаём представление, в котором будут детали конкретного отдельного товара
class PostDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'new.html'  # название шаблона будет product.html
    context_object_name = 'new'  # название объекта. в нём будет


class PostDetailView(DetailView):
    template_name = 'news/news_detail.html'
    queryset = Post.objects.all()


# дженерик для создания объекта. Надо указать только имя шаблона и класс формы, который мы написали в прошлом юните. Остальное он сделает за вас
class PostCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('news.create_post',)
    template_name = 'news/news_create.html'
    form_class = PostForm


class PostUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    template_name = 'news/news_create.html'
    form_class = PostForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class PostDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    template_name = 'news/news_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
