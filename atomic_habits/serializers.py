from rest_framework import serializers
from atomic_habits.models import Habit
from atomic_habits.validators import HabitValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'


class HabitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['id', 'location', 'time', 'action', 'is_nice_habit', 'related_habit', 'reward', 'time_to_complete',
                  'is_public']
        validators = [
            HabitValidator()
        ]
