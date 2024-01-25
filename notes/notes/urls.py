from django.contrib import admin
from django.urls import path, include

from blocks.views import pageNotFound, badRequest, forbidden, internalServerError

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blocks.urls')),
]

handler404 = pageNotFound
handler400 = badRequest
handler403 = forbidden
handler500 = internalServerError