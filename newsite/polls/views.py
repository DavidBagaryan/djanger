from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpRequest

from .models import Question


def index(request: HttpRequest):
    latest_question_list = get_list_or_404(Question)[:5]
    context = {'title': 'hello index', 'latest_question_list': latest_question_list}

    return render(request, 'polls/index.html', context)


def detail(request: HttpRequest, question_id: int):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request: HttpRequest, question_id: int):
    response = f"You're looking at the results of question {question_id}"
    context = {'title': f'{question_id} result', 'resp_str': response}

    return render(request, 'polls/result.html', context)


def vote(request: HttpRequest, question_id: int):
    response = f"You're voting on question {question_id}"
    context = {'title': f'{question_id} vote', 'resp_str': response}

    return render(request, 'polls/vote.html', context)
