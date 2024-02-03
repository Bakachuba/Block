from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from blocks.api.serializers import (IdeaSerializer, ListSerializer,
                                    SummarySerializer, WorkSerializer)
from blocks.models import Idea, List, Notes, Summary


class WorkAPITestCase(TestCase):
    def test_get(self):
        note_1 = Notes.objects.create(title='title1', content='content1')
        note_2 = Notes.objects.create(title='title2', content='content2')
        url = reverse('work-list')
        response = self.client.get(url)
        serializer_data = WorkSerializer([note_1, note_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


class IdeaAPITestCase(TestCase):
    def test_get(self):
        note_1 = Idea.objects.create(content='content1')
        note_2 = Idea.objects.create(content='content2')
        url = reverse('idea-list')
        response = self.client.get(url)
        serializer_data = IdeaSerializer([note_1, note_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


class SummaryAPITestCase(TestCase):
    def test_get(self):
        note_1 = Summary.objects.create(title='title1', content='content1', extension='1, 2, 3', explain='word1 word2')
        note_2 = Summary.objects.create(title='title2', content='content2', extension='1, 2, 3', explain='word1 word2')
        url = reverse('summary-list')
        response = self.client.get(url)
        serializer_data = SummarySerializer([note_1, note_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


class ListAPITestCase(TestCase):
    def test_get(self):
        note_1 = List.objects.create(title='title1', content='content1', status=True)
        note_2 = List.objects.create(title='title2', content='content2', status=False)
        url = reverse('list-list')
        response = self.client.get(url)
        serializer_data = ListSerializer([note_1, note_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)