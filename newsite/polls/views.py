from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader

from .models import Question


def index(request: HttpRequest) -> HttpResponse:
    latest_question_list = Question.objects.all()[:5]
    template = loader.get_template('polls/index.html')
    context = {'title': 'hello index', 'latest_question_list': latest_question_list}

    return HttpResponse(template.render(context, request))


def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f"You're looking at question {question_id}")


def results(request: HttpRequest, question_id: int) -> HttpResponse:
    # if not isinstance(question_id, str):
    #     raise Exception('common MFK!')

    response = f"You're looking at the results of question {question_id}"
    return HttpResponse(response)


def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f"You're voting on question {question_id}")
