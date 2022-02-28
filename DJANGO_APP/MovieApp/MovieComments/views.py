from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import messages
import requests

from .models import Movie
from . import forms


REST_URL = 'http://127.0.0.1:5000/predict'

def restSentiment(comment):
    response = requests.post(REST_URL, json={
        'comment': comment
    })
    return response.json()



def index(request):
    return render(request, 'index.html')


import pandas as pd
def movies(request):
    form = forms.ChooseMovie(request.POST or None)
    
    if form.is_valid():
        movie = form.cleaned_data.get("movie")

        data = Movie.objects.filter(movie=movie).values('movie', 'header_urls').distinct()

        context = {
                'form': form,
                'data': data,
            }
        return render(request, 'movies.html', context)

    data = Movie.objects.values('movie', 'header_urls').distinct()
    
    context = {
        'form': form,
        'data': data[:14]
    }
    return render(request, 'movies.html', context)





def addnewcomment(request):
    form = forms.AddNewComment(request.POST or None)
    if form.is_valid():
        movie = form.cleaned_data.get('movie')
        comment = form.cleaned_data.get('comment')

        sentiment = restSentiment( comment )['sentiment']

        header_urls = Movie.objects.filter(movie = movie).values('header_urls').first()['header_urls']

        new_comment = form.save(commit= False) # Because we didtn assigned author yet
        new_comment.sentiment = sentiment
        new_comment.header_urls = header_urls
        new_comment.save()

        messages.success(request, 'Your comment successfully added!')


        print(movie, comment, sentiment, header_urls)
        return redirect('movies')
    context = {
        'form': form
    }
    return render(request, 'addnewcomment.html', context)


def seeCommments(request, name):
    data0 = Movie.objects.filter(movie = name).count()
    data1 = Movie.objects.filter(movie = name).values('movie', 'header_urls').distinct()
    data2 = Movie.objects.filter(movie = name).values('comment', 'sentiment')
    
    context = {
        'data0': data0,
        'data1': data1,
        'data2': data2
    }
    return render(request, 'seecomments.html', context=context)
