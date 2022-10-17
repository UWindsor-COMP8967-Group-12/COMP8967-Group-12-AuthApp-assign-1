from django.urls import path, include
from .views import home, profile
from task.views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, TaskReorder
from django.contrib.auth.views import LogoutView
from users.views import CustomLoginView, RegisterView


urlpatterns = [
    # path('', home, name='users-home'),
    path('accounts/', include('allauth.urls')),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),

    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
]