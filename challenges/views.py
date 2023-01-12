from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenge = {
    "january":"Eat More Vegetables",
    "february":"Read 20 Minutes Everyday",
    "march":"Learn Django 20 Minutes everyday",
    "april":"Jogging 3 times a week",
    "may":"Eat More Vegetables",
    "june":"Read 20 Minutes Everyday",
    "july":"Learn Django 20 Minutes everyday",
    "august":"Jogging 3 times a week",
    "september":"Eat More Vegetables",
    "october":"Read 20 Minutes Everyday",
    "november":"Learn Django 20 Minutes everyday",
    "december": None,
}

# Create your views here.

def challenge_page(request):
    key_month = list(monthly_challenge.keys())

    return render(request, "challenges/challenge_list.html", {
        "months": key_month
    })

def monthly_challenge_by_number(request, month):
    key_month = list(monthly_challenge.keys())


    if (month > len(key_month)):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = key_month[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenge[month]
        capitalized_month = month.capitalize()
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": capitalized_month,
        })
    except:
        raise Http404()