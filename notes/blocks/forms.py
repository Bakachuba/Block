from django import forms
from .models import Notes, Summary, Periodic, List, Idea, Category


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
        fields = ['content', 'status', 'repetition_period', 'next_execution_time']
        labels = {
            'content': 'Содержание',
            'status': 'Статус',
            'repetition_period': 'Период повторения',
            'next_execution_time': 'Время следующего выполнения',
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
