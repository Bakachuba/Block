from django.shortcuts import render

from django.utils import timezone
from django.db import models
from blocks.models import Notes, Summary, Periodic, List, Idea


def index(request):
    return render(request, 'blocks/index.html')


def works(request):
    content = Notes.objects.order_by('-id')
    return render(request, 'blocks/works.html', {'title': 'Work notes', 'content': content})


def summary(request):
    text = Summary.objects.order_by('-id')
    return render(request, 'blocks/conspects.html', {'title': "Book's summary", 'text': text})


def periodic(request):
    current_time = timezone.now()
    period = Periodic.objects.annotate(
        time_difference=models.F('time_create') + models.F('time_period') - current_time).order_by('time_difference')

    return render(request, 'blocks/periodics.html', {'title': "Periodic tasks", 'period': period})


def list_view(request):
    lists = List.objects.order_by('-id')
    return render(request, 'blocks/lists.html', {'title': "Lists", 'lists': lists})


def idea(request):
    ideas = Idea.objects.order_by('id')
    return render(request, 'blocks/ideas.html', {'title': 'Ideas', 'ideas': ideas})