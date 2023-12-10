from rest_framework.serializers import ValidationError


class HabitValidator:

    def __call__(self, value):
        if value.get('related_habit') and value.get('reward'):
            raise ValidationError(
                'Запрещен одновременный выбор связанной привычки и указания вознаграждения'
            )
        if value.get('time_to_complete') > 120:
            raise ValidationError(
                'Время выполнения должно быть не больше 120 секунд'
            )
        if value.get('related_habit') and not value.get('related_habit').is_nice_habit:
            raise ValidationError(
                'В связанные привычки могут попадать только привычки с признаком приятной привычки'
            )
        if (value.get('is_nice_habit') and value.get('reward')) or (
                value.get('is_nice_habit') and value.get('related_habit')):
            raise ValidationError(
                'У приятной привычки не может быть вознаграждения или связанной привычки'
            )
