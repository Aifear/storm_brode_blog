from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Article


def landing(request):
    Articles = Article.objects.all()
    return render(request, 'landing/index.html', {'Articles':Articles})

def single(request, question_id):
    article = get_object_or_404(Article, pk=question_id)
    return render(request, 'landing/single.html', {'Article':article})
