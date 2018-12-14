from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest, lol: str, test: str) -> HttpResponse:
    return HttpResponse('Hello Julia from index!' + lol + test)


def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f"You're looking at question {question_id}")


def results(request: HttpRequest, question_id: int) -> HttpResponse:
    # if not isinstance(question_id, str):
    #     raise Exception('common MFK!')

    response = f"You're looking at the results of question {question_id}"
    return HttpResponse(response)


def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f"You're voting on question {question_id}")
