from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    
    
    '''
    $ render
    
    render를 사용하지 않을 때는 하단과 같이 사용할 수 있다.
    render에서 정의한 "months": months는 html에서 DTL를 이용해 값을 사용할 수 있다.
    
    months = list(monthly_challenges.keys())
    html_content = render_to_string("challenges/index.html", {
        "months": months
    })
    return HttpResponse(html_content) 
    '''
    
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month-1]
    
    '''
    $ reverse
    - reverse 내부를 확인한 결과, prefix를 갖고 오고, url pattern system에서 이 name이 있는지 확인하고 그 값을 갖고온다.
    - url pattern system에서 name이 동적 값으로 되어 있을 때 args에 있는 값을 넣는다.
    '''
    redirect_path = reverse("month-challenge", args=[redirect_month])

    '''
    $ redirect
    다른 Url에 pass하고 싶을 때 redirect를 이용해서 넘겨주면 된다.
    '''
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month: str):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month_name": month, 
            "text": challenge_text,
        })
    except:
        # 자동으로 templates에서 404.html 파일을 찾아줘서 반환시켜준다.
        return Http404()
        
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
