from django.urls import path
from . import views

urlpatterns=[
    # path("january", views.january),
    # path("february", views.february)
    path("", view=views.index, name="index"),
    
    # views에서 month를 변수로 사용할 수 있다. (* 단, variable 이름은 동일해야 한다.)
    # 이 month는 url에서 받은 parameter이다. ex) /challegnes/1 -> 1이 month
    # <int:month>처럼 paramter가 숫자일 때는 <int:month>와 matching 되고
    # string일 대는 <str:month>에 matching된다.
    path("<int:month>", view=views.monthly_challenge_by_number),
    path("<str:month>", view=views.monthly_challenge, name="month-challenge"),
]