from django.urls import path
from .views import DeleteView, TaskReorder
# from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
]