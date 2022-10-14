import imp
from urllib import response
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Meat free month",
    "febuary": "Walk 20 mins each day",
    "march": "20 mins Django every day",
    "april": "Meat free month",
    "may": "Walk 20 mins each day",
    "june": "20 mins Django every day",
    "july": "Meat free month",
    "august": "Walk 20 mins each day",
    "september": "20 mins Django every day",
    "october": "Meat free month",
    "november": "Walk 20 mins each day",
    "december": None
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challege_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challege_text,
            "month": month
        })
    except:
        raise Http404()
