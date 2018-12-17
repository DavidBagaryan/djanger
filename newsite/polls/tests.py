import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTest(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        plus_thirty_days = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=plus_thirty_days)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        one_day_ago = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=one_day_ago)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_last_day_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        last_day = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=last_day)
        self.assertIs(recent_question.was_published_recently(), True)
