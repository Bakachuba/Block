from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class TimestampedModel(models.Model):
    time_create = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class TitleContentModel(models.Model):
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class IsActive(models.Model):
    status = models.BooleanField(default=True)

    def toggle_active(self):
        self.status = not self.status
        self.save()

    class Meta:
        abstract = True


class Notes(TitleContentModel, TimestampedModel, IsActive):
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Summary(TitleContentModel, TimestampedModel):
    extension = models.CharField(max_length=255)
    explain = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Конспект'
        verbose_name_plural = 'Конспекты'


class Periodic(TimestampedModel, IsActive):
    content = models.TextField(blank=False)
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Периодическая задача'
        verbose_name_plural = 'Периодические задачи'


class Category(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class List(TitleContentModel, TimestampedModel, IsActive):
    group = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Список'
        verbose_name_plural = 'Списки'


class Idea(TimestampedModel, IsActive):
    content = models.TextField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def toggle_active(self):
        super().toggle_active()
        self.save()

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Идея'
        verbose_name_plural = 'Идеи'
