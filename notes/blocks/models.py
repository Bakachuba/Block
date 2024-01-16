from django.db import models


class Notes(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)


class Summary(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    extension = models.CharField(max_length=255)
    explain = models.TextField(blank=True)


class Periodic(models.Model):
    content = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_period = models.DurationField()


class Category(models.Model):
    name = models.CharField(max_length=255)


class List(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)


class Idea(models.Model):
    content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)