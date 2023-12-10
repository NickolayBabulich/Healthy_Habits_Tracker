from django.core.management import BaseCommand
from atomic_habits.services import MessageToTelegram


class Command(BaseCommand):

    def handle(self, *args, **options):
        testbot = MessageToTelegram()
        testbot.send('echo')
