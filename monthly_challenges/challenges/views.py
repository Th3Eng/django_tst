from tkinter import N
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# monthly challenges dictionary
months_list = {
    'january': 'Play the game of life.',
    'february': 'Write a program that prints out the numbers from 1 to 100.',
    'march': 'Watch the movie "The Matrix".',
    'april': 'sleep for at least 5 hours.',
    'may': 'Write a program that prints out the numbers from 1 to 100.',
    'june': 'Play the game of life.',
    'july': 'Write a program that prints out the numbers from 1 to 100.',
    'august': 'Watch the movie "The Matrix".',
    'september': 'sleep for at least 5 hours.',
    'october': 'Write a program that prints out the numbers from 1 to 100.',
    'november': 'Play the game of life.',
    'december': 'Write a program that prints out the numbers from 1 to 100.',
}


def index(request):
    months = ''
    for month in list(months_list.keys()):
        months += f"<li><a href='{reverse('challenges_path', kwargs={'month': month})}'>{month}</a></li>"

    response_data = f"<ul>{months}</ul>"
    return HttpResponse(response_data)


def months(request, month):
    """_summary_: recieves a month and returns the corresponding month.

    Args:
        request (): request object
        month (months_list element): month

    Returns:
        HttpResponse: response object
    """
    if month in months_list:
        return HttpResponse(f"<h1>You're looking at the {month} challenge.\n {months_list[month]}</h1>")
    else:
        return HttpResponseNotFound("Month not found.")


def months_by_num(request, month):
    """_summary_:recieves a number of month and returns the corresponding month.

    Args:
        request (): request object
        num (int): number of month

    Returns:
        HttpResponse: response object
    """
    months = list(months_list.keys())
    if month in range(1, months.__len__() + 1):
        # get the redirect url path
        redirect_path = reverse('challenges_path', kwargs={
                                'month': months[month - 1]})
        return HttpResponseRedirect(redirect_path)
    else:
        return HttpResponseNotFound("Month not found.")
