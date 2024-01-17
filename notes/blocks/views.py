from django.shortcuts import render, redirect

from django.utils import timezone
from django.db import models

from blocks.forms import NotesForm, SummaryForm, PeriodicForm, ListForm, IdeaForm, CategoryForm
from blocks.models import Notes, Summary, Periodic, List, Idea, Category


def index(request):
    return render(request, 'blocks/index.html')


def works(request):
    content = Notes.objects.order_by('-id')

    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('works')  # Предположим, что у вас есть URL с именем 'works'
    else:
        form = NotesForm()

    return render(request, 'blocks/works.html', {'title': 'Work notes', 'content': content, 'form': form})


def summary(request):
    text = Summary.objects.order_by('-id')

    if request.method == 'POST':
        form = SummaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('summary')  # Предположим, что у вас есть URL с именем 'works'
    else:
        form = SummaryForm()

    return render(request, 'blocks/conspects.html', {'title': "Book's summary", 'text': text, 'form': form})


def periodic(request):
    current_time = timezone.now()
    period = Periodic.objects.annotate(
        time_difference=models.F('time_create') + models.F('time_period') - current_time).order_by('time_difference')

    if request.method == 'POST':
        form = PeriodicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('periodic')  # Предположим, что у вас есть URL с именем 'works'
    else:
        form = PeriodicForm()

    return render(request, 'blocks/periodics.html', {'title': "Periodic tasks", 'period': period, 'form': form})


def list_view(request):
    lists = List.objects.order_by('group')

    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lists')  # Предположим, что у вас есть URL с именем 'works'
    else:
        form = ListForm()

    return render(request, 'blocks/lists.html', {'title': "Lists", 'lists': lists, 'form': form})


def cat(request):
    cat = Category.objects.order_by('id')

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lists')  # Assuming you have a URL named 'lists'
    else:
        form = CategoryForm()

    second_form = CategoryForm()

    return render(request, 'blocks/lists.html', {'form': form, 'second_form': second_form, 'cat': cat})

def idea(request):
    ideas = Idea.objects.order_by('id')

    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ideas')  # Предположим, что у вас есть URL с именем 'works'
    else:
        form = IdeaForm()

    return render(request, 'blocks/ideas.html', {'title': 'Ideas', 'ideas': ideas, 'form': form})
