from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from blocks.views import (badRequest, forbidden, internalServerError,
                          pageNotFound)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blocks.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += staticfiles_urlpatterns()

handler404 = pageNotFound
handler400 = badRequest
handler403 = forbidden
handler500 = internalServerError
