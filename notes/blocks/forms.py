from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Category, Idea, List, Notes, Periodic, Summary


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content', 'status']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Опишите задачу'}),
        }
        labels = {
            'title': 'Тема',
            'content': 'Задача',
            'status': 'Активна',
        }


class SummaryForm(forms.ModelForm):
    class Meta:
        model = Summary
        fields = ['title', 'content', 'extension', 'explain']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Основные мысли'}),
            'explain': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Итоги'}),
        }
        labels = {
            'title': 'Тема',
            'content': 'Основные мысли',
            'extension': 'Ключевые слова',
            'explain': 'Итоги',
        }


class PeriodicForm(forms.ModelForm):
    class Meta:
        model = Periodic
        fields = ['content', 'status', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
                  'sunday']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Опишите задачу'}),
        }
        labels = {
            'content': 'Задача',
            'status': 'Активна',
            'monday': 'Каждый понедельник',
            'tuesday': 'Каждый вторник',
            'wednesday': 'Каждую среду',
            'thursday': 'Каждый четверг',
            'friday': 'Каждую пятницу',
            'saturday': 'Каждую субботу',
            'sunday': 'Каждое воскресенье',
        }


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['title', 'content', 'status', 'group']
        widgets = {
            'content': forms.Textarea(
                attrs={'rows': 4, 'placeholder': 'Создайте полный список или отдельную его часть'}),
        }
        labels = {
            'title': 'Тема',
            'content': 'Содержание',
            'status': 'Активна',
            'group': 'Категория',
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Создание категории списка'}),
        }
        labels = {
            'name': 'Название категории',
        }


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['content', 'status']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Опишите свою идею или введите ключевые слова'}),
        }
        labels = {
            'content': 'Идея',
            'status': 'Активна',
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
