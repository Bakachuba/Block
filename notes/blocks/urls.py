from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView

from . import views
from .views import IdeaAPI, WorkAPI, ListAPI, SummaryAPI, PeriodicAPI, profile_view, RegisterView

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

    path('api/drf-auth/', include('rest_framework.urls')),
    # session based
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    # djoser based
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # jwt based
    path('profile', profile_view, name='profile'),
    path('register', RegisterView.as_view(), name='register'),
]
