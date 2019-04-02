from django.urls import path, re_path, include
#from .views import poll_detail, poll_list
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote

urlpatterns = [
    # path("pols/", poll_list, name="poll_list"),
    # path("polls/<int:pk>/", poll_detail, name="polls_detail"),

    
    path("polls/", PollList.as_view(), name="poll_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("vote/", CreateVote.as_view(), name="create_vote"),
    path("choices/", ChoiceList.as_view(), name="choice_list"),

]
