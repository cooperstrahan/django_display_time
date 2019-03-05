from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    elif 'count' in request.session:
        request.session['count'] += 1
    data = {
        "rand": get_random_string(length=14)
    }
    return render(request, 'app_random_words/index.html', data)

def reset(request):
    request.session.flush()
    return redirect('/random_word')
