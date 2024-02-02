import logging
import pdb
import traceback

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import requests
from django.urls import reverse

from django.utils import timezone
from django.db import models
from django.views.generic import CreateView, FormView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from blocks.api.serializers import IdeaSerializer, WorkSerializer, PeriodicSerializer, ListSerializer, SummarySerializer
from blocks.forms import NotesForm, SummaryForm, PeriodicForm, ListForm, IdeaForm, CategoryForm, RegisterForm
from blocks.models import Notes, Summary, Periodic, List, Idea, Category
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status

from blocks.permissions import IsAdminOrReadOnly

logger = logging.getLogger('main')


# Основная страница
def index(request):
    logger.info('start home page')
    return render(request, 'blocks/index.html')


# Страница с задачами
@login_required
def works(request):
    # Получаем список задач, сортируем по убыванию идентификаторов
    content = Notes.objects.filter(user=request.user).order_by('-id')

    if request.method == 'POST':
        logger.info('Creating work note')
        # Если запрос POST, создаем форму и сохраняем задачу, если форма валидна
        form = NotesForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('works')  # Перенаправление на страницу с задачами после сохранения
    else:
        form = NotesForm()

    # Отображение страницы с задачами
    return render(request, 'blocks/works.html', {'title': 'Work notes', 'content': content, 'form': form})


# Страница с конспектами
@login_required
def summary(request):
    # Получаем список конспектов, сортируем по убыванию идентификаторов
    text = Summary.objects.filter(user=request.user).order_by('-id')

    if request.method == 'POST':
        logger.info('Creating summary note')
        # Если запрос POST, создаем форму и сохраняем конспект, если форма валидна
        form = SummaryForm(request.POST)
        if form.is_valid():
            summary = form.save(commit=False)
            summary.user = request.user
            summary.save()
            return redirect('summary')  # Перенаправление на страницу с конспектами после сохранения
    else:
        form = SummaryForm()

    # Отображение страницы с конспектами
    return render(request, 'blocks/conspects.html', {'title': "Book's summary", 'text': text, 'form': form})


# API для конспектов
class SummaryAPI(viewsets.ModelViewSet):
    logger.info('Open summarys api')
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

    def perform_create(self, serializer):
        # Associate the summary with the currently logged-in user
        serializer.save(user=self.request.user)


# Страница с периодическими задачами
@login_required
def periodic(request):
    if request.method == 'POST':
        form = PeriodicForm(request.POST)
        if form.is_valid():
            periodic = form.save(commit=False)
            periodic.days_of_week = ', '.join(form.cleaned_data['days_of_week'])
            periodic.user = request.user
            periodic.save()
            return redirect('periodic')

    else:
        form = PeriodicForm()

    return render(request, 'blocks/periodics.html', {'form': form})


# API для периодических задач
class PeriodicAPI(viewsets.ModelViewSet):
    logger.info('Open periodics api')
    queryset = Periodic.objects.all()
    serializer_class = PeriodicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

    def perform_create(self, serializer):
        # Associate the periodic task with the currently logged-in user
        serializer.save(user=self.request.user)


# Страница со списками
@login_required
def list_view(request):
    # Получаем списки, отфильтрованные по статусу и отсортированные по группе
    lists = List.objects.filter(user=request.user, status=True).order_by('group')
    form = ListForm()
    category_form = CategoryForm()

    if request.method == 'POST':
        logger.info('Creating list note')
        # Если запрос POST, создаем форму и сохраняем список, если форма валидна
        if 'note_form' in request.POST:
            form = ListForm(request.POST)
            if form.is_valid():
                note = form.save(commit=False)
                note.user = request.user
                note.save()
                return redirect('lists')

        # Если запрос POST, создаем форму и сохраняем категорию, если форма валидна
        elif 'category_form' in request.POST:
            category_form = CategoryForm(request.POST)
            if category_form.is_valid():
                category = category_form.save(commit=False)
                category.user = request.user
                category.save()
                return redirect('lists')

    # Отображение страницы со списками
    return render(request, 'blocks/lists.html',
                  {'title': "Lists", 'lists': lists, 'form': form, 'category_form': category_form})


# API для списков
class ListAPI(viewsets.ModelViewSet):
    logger.info('Open lists api')
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

    def perform_create(self, serializer):
        # Associate the list with the currently logged-in user
        serializer.save(user=self.request.user)


# Страница с идеями
@login_required
def idea(request):
    # Получаем список идей, отсортированных по идентификаторам
    ideas = Idea.objects.filter(user=request.user).order_by('id')

    if request.method == 'POST':
        logger.info('Creating idea note')
        # Если запрос POST, создаем форму и сохраняем идею, если форма валидна
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.user = request.user
            idea.save()
            return redirect('ideas')
    else:
        form = IdeaForm()

    # Отображение страницы с идеями
    return render(request, 'blocks/ideas.html', {'title': 'Ideas', 'ideas': ideas, 'form': form})


# API для идей
class IdeaAPI(viewsets.ModelViewSet):
    logger.info('Open ideas api')
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

    def perform_create(self, serializer):
        # Associate the idea with the currently logged-in user
        serializer.save(user=self.request.user)


# API для задач
class WorkAPI(viewsets.ModelViewSet):
    logger.info('Open works api')
    queryset = Notes.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

    def perform_create(self, serializer):
        # Associate the note with the currently logged-in user
        serializer.save(user=self.request.user)


def pageNotFound(request, *args, **kwargs):
    logger.info('Page not found 404')
    return render(request, 'blocks/404.html')


def badRequest(request, *args, **kwargs):
    logger.info('Bad request 400')
    return render(request, 'blocks/400.html')


def forbidden(request, *args, **kwargs):
    logger.info('Forbidden 403')
    return render(request, 'blocks/403.html')


def internalServerError(request, *args, **kwargs):
    logger.info('Internal server error 500')
    return render(request, 'blocks/500.html')


@login_required
def profile_view(request):
    return render(request, 'blocks/profile.html')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Registration successful. Please log in.')

        # Перенаправляем пользователя на страницу входа (или куда вы считаете нужным)
        return redirect(reverse('login'))