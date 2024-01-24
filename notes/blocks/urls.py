from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import IdeaAPI, WorkAPI, ListAPI, SummaryAPI, PeriodicAPI

router = DefaultRouter()

router.register(r'ideas', IdeaAPI, basename='idea')
router.register(r'works', WorkAPI, basename='work')
router.register(r'lists', ListAPI, basename='list')
router.register(r'summarys', SummaryAPI, basename='summary')
router.register(r'periodics', PeriodicAPI, basename='periodic')

urlpatterns = [
    path('', views.index, name='home'),
    path('works', views.works, name='works'),
    path('summary', views.summary, name='summary'),
    path('periodic', views.periodic, name='periodic'),
    path('lists', views.list_view, name='lists'),
    path('ideas', views.idea, name='ideas'),
    path('api/', include(router.urls)),
]
