from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from atomic_habits.permissions import IsOwner
from atomic_habits.serializers import HabitSerializer, HabitCreateSerializer
from atomic_habits.models import Habit
from atomic_habits.paginators import Paginator


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = Paginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if not Habit.objects.all().filter(owner=self.request.user):
            raise ValueError('В списке еще нет ни одной привычки!')
        else:
            return Habit.objects.filter(owner=self.request.user)


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class PublicHabitsAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all().filter(is_public=True)
