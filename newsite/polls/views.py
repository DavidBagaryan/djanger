from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpRequest

from .models import Question


def index(request: HttpRequest):
    latest_question_list = get_list_or_404(Question)[:5]  # Question.objects.all()[:5]
    context = {'title': 'hello index', 'latest_question_list': latest_question_list}

    return render(request, 'polls/index.html', context)


def detail(request: HttpRequest, question_id: int):
    question = get_object_or_404(Question, pk=question_id)

    # try:
    #     question = Question.objects.get(id=question_id)
    # except Question.DoesNotExist:
    #     raise Http404(f'Question {question_id} not found')

    # resp_str = f"You're looking at question {question_id}"
    # context = {'title': f'{question_id} details', 'resp_str': resp_str}

    return render(request, 'polls/detail.html', {'question': question})


def results(request: HttpRequest, question_id: int):
    response = f"You're looking at the results of question {question_id}"
    context = {'title': f'{question_id} result', 'resp_str': response}

    return render(request, 'polls/result.html', context)


def vote(request: HttpRequest, question_id: int):
    response = f"You're voting on question {question_id}"
    context = {'title': f'{question_id} vote', 'resp_str': response}

    return render(request, 'polls/vote.html', context)
