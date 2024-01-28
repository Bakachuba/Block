from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from blocks.views import pageNotFound, badRequest, forbidden, internalServerError

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blocks.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]

urlpatterns += staticfiles_urlpatterns()

handler404 = pageNotFound
handler400 = badRequest
handler403 = forbidden
handler500 = internalServerError
