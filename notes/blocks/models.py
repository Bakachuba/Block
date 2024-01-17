from django.db import models


class TimestampedModel(models.Model):
    time_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class TitleContentModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)

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
    time_period = models.DurationField()

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

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Идея'
        verbose_name_plural = 'Идеи'
