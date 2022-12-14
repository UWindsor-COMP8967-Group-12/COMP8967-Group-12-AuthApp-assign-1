from django.contrib import admin

from django.urls import path, include
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from users.views import CustomLoginView, ResetPasswordView, ChangePasswordView

from users.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('tasks/',include('task.urls')),
    path('photos/', include('photos.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
