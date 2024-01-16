from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('works', views.works, name='works'),
    path('summary', views.summary, name='summary'),
    path('periodic', views.periodic, name='periodic'),
    path('lists', views.list_view, name='lists'),
    path('ideas', views.idea, name='ideas'),
]
