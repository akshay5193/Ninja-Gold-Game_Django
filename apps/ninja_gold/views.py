from django.shortcuts import render, redirect, HttpResponse
import random

# Create your views here.


def index(request):
    if 'gold' in request.session:
        request.session['gold'] += 0

    else:
        request.session['gold'] = 1

    if request.session['gold'] > 0:
        request.session['earning'] = random.randint(1, 21)
        print(request.session['earning'])
    return render(request, "ninja_gold/index.html")


def farm(request):
    if request.method == 'POST':
        if request.POST == "farm":
            request.session['gold'] += request.session['score']
            print(request.session['gold'])
    return redirect('/')
