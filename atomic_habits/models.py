from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    location = models.CharField(max_length=150, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    action = models.CharField(max_length=150, verbose_name='Действие')
    is_nice_habit = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('Habit', on_delete=models.CASCADE, verbose_name='Связанная привычка', **NULLABLE)
    periodicity = models.PositiveIntegerField(default=1, verbose_name='Периодичность', **NULLABLE)
    reward = models.CharField(max_length=150, verbose_name='Вознаграждение', **NULLABLE)
    time_to_complete = models.PositiveIntegerField(verbose_name='Время на выполнение', **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    def __str__(self):
        return f'{self.action} - {self.time} - {self.location}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
