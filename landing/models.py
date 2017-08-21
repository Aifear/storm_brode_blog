from django.contrib.auth.models import User
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    present_page_text = models.CharField(max_length=200, default='')
    text = models.TextField()
    user = models.ForeignKey(User)
    date = models.DateField(default = '2017-01-01')

    def __str__(self):
        return self.title

    def next(self):
        Articles = Article.objects.all()
        if len(Articles) > self.id:
            return self.id+1
        else:
            return 1

    def next_title(self):
        Articles = Article.objects.all()
        id = self.next()
        return Articles[id-1].title

    def next_pres_text(self):
        Articles = Article.objects.all()
        id = self.next()
        return Articles[id - 1].present_page_text


    def prev(self):
        if self.id == 1:
            Articles = Article.objects.all()
            return len(Articles)
        else:
            return self.id - 1

    def prev_title(self):
        Articles = Article.objects.all()
        id = self.prev()
        return Articles[id - 1].title

    def prev_pres_text(self):
        Articles = Article.objects.all()
        id = self.prev()
        return Articles[id - 1].present_page_text