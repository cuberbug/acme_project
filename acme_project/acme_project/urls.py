from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('pages.urls', namespace='pages')),
    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls', namespace='birthday')),
]
