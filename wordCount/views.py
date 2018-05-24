from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')


def count(request):

    fulltext = request.GET["fulltext"]

    mytext = fulltext.split()

    wordcount = {}

    for word in mytext:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1

    sorted_word_count = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True )

    return render(request, 'count.html', {"sortedwords" : sorted_word_count})


def about(request):
    return render(request, 'about.html')

