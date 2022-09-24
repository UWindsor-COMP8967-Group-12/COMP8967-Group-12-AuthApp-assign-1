from django.urls import path, include
from .views import home, profile, RegisterView

urlpatterns = [
    path('', home, name='users-home'),
    path('accounts/', include('allauth.urls')),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
]
