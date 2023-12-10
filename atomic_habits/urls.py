from django.urls import path
from atomic_habits.apps import AtomicHabitsConfig
from atomic_habits.views import (
    HabitListAPIView,
    HabitCreateAPIView,
    HabitRetrieveAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView,
    PublicHabitsAPIView
)

app_name = AtomicHabitsConfig.name

urlpatterns = [
    path('habits/', HabitListAPIView.as_view(), name='list_of_habits'),
    path('habits/create/', HabitCreateAPIView.as_view(), name='create_a_habit'),
    path('habits/view/<int:pk>', HabitRetrieveAPIView.as_view(), name='show_habit'),
    path('habits/edit/<int:pk>', HabitUpdateAPIView.as_view(), name='edit_habit'),
    path('habits/delete/<int:pk>', HabitDestroyAPIView.as_view(), name='delete_habit'),
    path('habits/public/', PublicHabitsAPIView.as_view(), name='public_habits'),
]
