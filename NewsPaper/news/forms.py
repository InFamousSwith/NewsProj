from .models import Post
from django.core.validators import MinLengthValidator

from django.forms import ModelForm, CharField


class PostForm(ModelForm):

    title = CharField(label="Заголовок", min_length=5)
    text = CharField(label="Статья", min_length=10)

    class Meta:
        model = Post
        fields = ['author', "title", 'text', 'post']

        labels = {
            'post': 'Тип',
        }