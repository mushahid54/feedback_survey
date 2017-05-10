import random

__author__ = 'Mushahid Khan'
from django.core.management.base import BaseCommand, CommandError
from feedback_survey.models import FeedbackTemplate


class Command(BaseCommand):

    help = "have to check this command not completed"

    def handle(self, *args, **options):
        for feedback in range(1, 6):
            feedback_type = random.choice(["Text", "Multi", "Single", "Short", "Long"])
            feedback = FeedbackTemplate.objects.create(name=feedback_type)


