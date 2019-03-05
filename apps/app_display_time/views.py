from django.shortcuts import render
from time import gmtime, strftime, localtime

def index(request):
    context = {
        "date": strftime("%b %d, %Y", localtime()),
        "hour": strftime("%-I:%M %p", localtime())

    }
    return render(request, 'app_display_time/index.html', context)
