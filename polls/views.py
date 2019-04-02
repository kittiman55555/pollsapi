from django.shortcuts import render, get_object_or_404
from .models import Poll
from django.http import JsonResponse
# Create your views here.

def poll_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {
        "results" : list(polls.values(
            "question","create_by__username","pub_date"
            )
        )
    }
    return JsonResponse(data)


def poll_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {
        "results" : {
            "question" : poll.question,
            "create_by" : poll.create_by.username,
            "pub_date" : poll.pub_date
        }
    }
    return JsonResponse(data)