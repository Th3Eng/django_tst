from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

months_list = [
    'january',
    'february',
    'march',
    'spril',
    'may',
    'june',
    'july',
    'august',
    'september',
    'october',
    'november',
    'december',
]

months_challenge_text = ['Challenge 1', 'Challenge 2', 'Challenge 3', 'Challenge 4', 'Challenge 5', 'Challenge 6',
                         'Challenge 7', 'Challenge 8', 'Challenge 9', 'Challenge 10', 'Challenge 11', 'Challenge 12', ]


def index(request):
    return HttpResponse("Hello, world. You're at the monthly_challenges index.")


def months(request, month):
    if month in months_list:
        return HttpResponse(f"You're looking at the {month} challenge.\n {months_challenge_text[months_list.index(month)]}")
    else:
        return HttpResponseNotFound("Month not found.")
