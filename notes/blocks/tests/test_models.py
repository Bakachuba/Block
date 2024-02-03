from django.test import TestCase
from django.utils import timezone

from blocks.models import Category, Idea, List, Notes, Periodic, Summary


class NotesModelTestCase(TestCase):
    def test_create_notes(self):
        notes = Notes.objects.create(title='Test Title', content='Test Content')
        self.assertEqual(notes.title, 'Test Title')
        self.assertEqual(notes.content, 'Test Content')
        self.assertTrue(notes.status)  # Assuming IsActive default is True


class SummaryModelTestCase(TestCase):
    def test_create_summary(self):
        summary = Summary.objects.create(title='Test Title', content='Test Content', extension='txt',
                                         explain='Test Explain')
        self.assertEqual(summary.title, 'Test Title')
        self.assertEqual(summary.content, 'Test Content')
        self.assertEqual(summary.extension, 'txt')
        self.assertEqual(summary.explain, 'Test Explain')


class PeriodicModelTestCase(TestCase):
    def test_create_periodic(self):
        periodic = Periodic.objects.create(content='Test Content', repetition_period=60)
        self.assertEqual(periodic.content, 'Test Content')
        self.assertEqual(periodic.repetition_period, 60)
        self.assertIsNotNone(periodic.next_execution_time)


class CategoryModelTestCase(TestCase):
    def test_create_category(self):
        category = Category.objects.create(name='Test Category')
        self.assertEqual(category.name, 'Test Category')


class ListModelTestCase(TestCase):
    def test_create_list(self):
        category = Category.objects.create(name='Test Category')
        test_list = List.objects.create(title='Test Title', content='Test Content', group=category)
        self.assertEqual(test_list.title, 'Test Title')
        self.assertEqual(test_list.content, 'Test Content')
        self.assertTrue(test_list.status)
        self.assertEqual(test_list.group, category)


class IdeaModelTestCase(TestCase):
    def test_create_idea(self):
        idea = Idea.objects.create(content='Test Content')
        self.assertEqual(idea.content, 'Test Content')
        self.assertTrue(idea.status)
