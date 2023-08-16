from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from users import router as users_router


auth_urlpatterns = []

api_urlpatterns = [
    path('auth/', include(auth_urlpatterns)),
    path('users/', include(users_router.router.urls)),
]

if settings.DEBUG:
    auth_urlpatterns.append(
        path('verify/', include('rest_framework.urls')),
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
]
