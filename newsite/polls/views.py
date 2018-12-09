from django.shortcuts import render
from django.http import HttpResponse


def index(request, lol, test):
    return HttpResponse('Hello Julia from index!' + lol + test)
