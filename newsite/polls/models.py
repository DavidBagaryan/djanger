import datetime

from django.db import models
from django.db.models import CharField
from django.utils import timezone, dateparse


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self) -> CharField:
        return self.question_text

    def was_published_recently(self) -> bool:
        now = timezone.now()
        pub_date = dateparse.parse_datetime(self.pub_date.__str__())
        return now - datetime.timedelta(days=1) <= pub_date <= now
        # return 'yes' if (now - datetime.timedelta(days=1) <= pub_date <= now) else 'no'

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> CharField:
        return self.choice_text
