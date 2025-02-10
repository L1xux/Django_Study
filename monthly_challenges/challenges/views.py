from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
# def january(request):
#     return HttpResponse("Walk for at least 20 minutes every day!")

# def february(request):
#     return HttpResponse("Eat no meat for the entire month!")

# def march(request):
#     return HttpResponse("No exercise! :D")

monthly_challenges = {
    "january": "Eat no meat!",
    "february": "Walk for at least 20 mins",
    "march": "Learn a course",
    "april": "Eat",
    "may": "Walk",
    "june": "Learn",
    "july": "Eat",
    "august": "Walk",
    "september": "Learn",
    "october": "Eat",
    "november": "Walk",
    "december": "Learn"
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"
        
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month: str):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month is not supported")
