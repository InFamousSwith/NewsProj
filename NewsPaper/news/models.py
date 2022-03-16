from django.contrib.auth.models import User
from django.db import models


# one_to_one_relation = models.OneToOneField(some_model)
# one_to_many_relation = models.ForeignKey(some_model)
# many_to_many_relation = models.ManyToManyField(some_model)

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    # def update_rating(self):
    # post_rating = Post.objects.filter(author=self).values('rating')

    # post_rating = sum(rate['rating'] for rate in post_rating) * 3

    # news_comments_rating = Post.objects.filter(author=self).values('post__rating')

    def update_rating(self, new_rating):
        self.rating = new_rating
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    article = 'AR'
    news = 'NE'
    Posts = [
        (article, 'статья'),
        (news, 'новость')
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.CharField(max_length=2, choices=Posts, default=article)
    time_in = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[:124] + '...'

    def __str__(self):
        if self.post == self.article:
            return f'{self.Posts[0][1]}: {self.title}'
        else:
            return f'{self.Posts[1][1]}: {self.title}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/news/{self.id}'

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
