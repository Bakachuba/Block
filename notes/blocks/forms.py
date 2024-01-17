from django import forms
from .models import Notes, Summary, Periodic, List, Idea, Category


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content', 'status']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),

        }


class SummaryForm(forms.ModelForm):
    class Meta:
        model = Summary
        fields = ['title', 'content', 'extension', 'explain']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
            'explain': forms.Textarea(attrs={'rows': 4}),
        }


class PeriodicForm(forms.ModelForm):
    class Meta:
        model = Periodic
        fields = ['content', 'time_period']


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['title', 'content', 'status', 'group']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['content', 'status']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }
