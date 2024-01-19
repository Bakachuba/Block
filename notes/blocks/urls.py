from django.urls import path

from . import views
from .views import IdeaAPI, WorkAPI, IdeaAPIUpdate, WorkAPIUpdate

urlpatterns = [
    path('', views.index, name='home'),
    path('works', views.works, name='works'),
    path('summary', views.summary, name='summary'),
    path('periodic', views.periodic, name='periodic'),
    path('lists', views.list_view, name='lists'),
    path('ideas', views.idea, name='ideas'),
    path('api/ideas/', IdeaAPI.as_view(), name='idea-list-api'),
    path('api/ideas/<int:pk>/', IdeaAPIUpdate.as_view(), name='idea-detail-api'),
    path('api/works/', WorkAPI.as_view(), name='work-list-api'),
    path('api/works/<int:pk>/', WorkAPIUpdate.as_view(), name='work-detail-api'),

]
