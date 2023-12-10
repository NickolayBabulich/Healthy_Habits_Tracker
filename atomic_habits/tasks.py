import datetime
from celery import shared_task
from django.utils import timezone
from atomic_habits.models import Habit
from atomic_habits.services import MessageToTelegram


@shared_task
def habits_worker():
    now = datetime.datetime.now()
    now = timezone.make_aware(now, timezone.get_current_timezone())
    now += datetime.timedelta(minutes=10)
    habits = Habit.objects.all()
    reminder = MessageToTelegram()

    for habit in habits:
        message = f"В {habit.time.strftime('%H:%M')} я буду {habit.action} в {habit.location}"
        if not habit.is_nice_habit and now.hour == habit.time.hour and now.minute == habit.time.minute:
            reminder.send(message)
