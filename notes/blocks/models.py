from django.db import models
from django.utils import timezone


class TimestampedModel(models.Model):
    time_create = models.DateTimeField(auto_now_add=True)

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
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Summary(TitleContentModel, TimestampedModel):
    extension = models.CharField(max_length=255)
    explain = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Конспект'
        verbose_name_plural = 'Конспекты'


class Periodic(TimestampedModel):
    content = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    repetition_period = models.IntegerField(null=True, blank=True)
    # Поле, которое будет хранить периодичность в секундах
    next_execution_time = models.DateTimeField(null=True, blank=True)
    # Поле, которое будет хранить время следующего запланированного выполнения

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Если установлено значение repetition_period и next_execution_time не задано,
        # устанавливаем next_execution_time на текущее время плюс repetition_period
        if self.repetition_period is not None and self.next_execution_time is None:
            self.next_execution_time = timezone.now() + timezone.timedelta(seconds=self.repetition_period)
            self.save()

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Периодическая задача'
        verbose_name_plural = 'Периодические задачи'


class Category(models.Model):
    name = models.CharField(max_length=255)

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




# def application(environ, start_response):
#     if environ.get('PATH_INFO') == '/':
#         status = '200 OK'
#         content = HELLO_WORLD
#     else:
#         status = '404 NOT FOUND'
#         content = 'Page not found.'
#     response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(content)))]
#     start_response(status, response_headers)
#     yield content.encode('utf8')
