from django.http import JsonResponse
from django.shortcuts import render, redirect
import requests

from django.utils import timezone
from django.db import models
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from blocks.api.serializers import IdeaSerializer, WorkSerializer, PeriodicSerializer, ListSerializer, SummarySerializer
from blocks.forms import NotesForm, SummaryForm, PeriodicForm, ListForm, IdeaForm, CategoryForm
from blocks.models import Notes, Summary, Periodic, List, Idea, Category
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status

from blocks.permissions import IsAdminOrReadOnly


def index(request):
    return render(request, 'blocks/index.html')


def works(request):
    content = Notes.objects.order_by('-id')

    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('works')  # Assuming you have a URL named 'works'
    else:
        form = NotesForm()

    return render(request, 'blocks/works.html', {'title': 'Work notes', 'content': content, 'form': form})


def summary(request):
    text = Summary.objects.order_by('-id')

    if request.method == 'POST':
        form = SummaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('summary')  # Assuming you have a URL named 'summary'
    else:
        form = SummaryForm()

    return render(request, 'blocks/conspects.html', {'title': "Book's summary", 'text': text, 'form': form})


class SummaryAPI(viewsets.ModelViewSet):
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

# class PeriodicView(ModelViewSet)
#прочитать позже

def periodic(request):
    current_time = timezone.now()
    period = Periodic.objects.all()

    for task in period:
        task.time_difference = task.time_create + task.repetition_period - current_time
        task.is_overdue = task.time_difference.total_seconds() < 0

    if request.method == 'POST':
        form = PeriodicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('periodic')  # Assuming you have a URL named 'periodic'
    else:
        form = PeriodicForm()

    return render(request, 'blocks/periodics.html', {'title': "Periodic tasks", 'period': period, 'form': form})


class PeriodicAPI(viewsets.ModelViewSet):
    queryset = Periodic.objects.all()
    serializer_class = PeriodicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]


def list_view(request):
    lists = List.objects.filter(status=True).order_by('group')
    form = ListForm()
    category_form = CategoryForm()

    if request.method == 'POST':
        if 'note_form' in request.POST:
            form = ListForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lists')

        elif 'category_form' in request.POST:
            category_form = CategoryForm(request.POST)
            if category_form.is_valid():
                category_form.save()
                return redirect('lists')

    return render(request, 'blocks/lists.html',
                  {'title': "Lists", 'lists': lists, 'form': form, 'category_form': category_form})


class ListAPI(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]


def idea(request):
    ideas = Idea.objects.order_by('id')

    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ideas')
    else:
        form = IdeaForm()

    return render(request, 'blocks/ideas.html', {'title': 'Ideas', 'ideas': ideas, 'form': form})


class IdeaAPI(viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]


def update_idea_status(request, idea_id):
    try:
        idea = Idea.objects.get(id=idea_id)
        idea.toggle_active()
        return JsonResponse({'success': True})
    except Idea.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Idea not found'})


class WorkAPI(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]
