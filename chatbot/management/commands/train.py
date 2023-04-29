from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ListTrainer
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Training the chatterbot"

    def handle(self, *args, **options):
        chatterbot = ChatBot(**settings.CHATTERBOT)
        trainer = ListTrainer(chatterbot)
        trainer.train(
            [
                "Hello",
                "Hi There",
                "How are you doing?",
                "Im doing great",
                "That is great to hear." "Thank you.",
                "You're welcome.",
            ]
        )
        self.stdout.write(self.style.SUCCESS("Successfull!"))
