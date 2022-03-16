from django_filters import FilterSet, DateFilter, \
    ChoiceFilter, CharFilter  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post


# создаём фильтр
class PostFilter(FilterSet):
    time_in = DateFilter(field_name='time_in', lookup_expr='gt', label='Опубликовано после ')
    title = CharFilter(label='Заголовок')

    class Meta:
        model = Post
        fields = ['author__user', 'title', 'time_in']