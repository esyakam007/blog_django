from django.shortcuts import render, get_object_or_404
from .models import News


def news_list(request):
    #Вывод всех статей
    news = News.objects.all()
    return render(request, 'news/news_list.html', {'news': news})


def news_single(request, pk):
    #Вывод одной статьи
    new = get_object_or_404(News, id=pk)
    return render(request, 'news/news_single.html', {'new': new})