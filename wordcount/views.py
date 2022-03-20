from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def count(request):
    fulltext = request.GET["fulltext"]

    fulltext_list = fulltext.split(' ')

    qtd = len(fulltext_list)

    fulltext_words = Counter(fulltext_list)

    context = {
        "fulltext": fulltext,
        "words": fulltext_list,
        "statistic": fulltext_words,
        "number_words": qtd,
    }
    return render(request, "count.html", context)
