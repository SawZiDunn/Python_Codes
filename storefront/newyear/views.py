from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

# Create your views here.


def index(request):
    now = datetime.now()

    return render(request, 'newyear/index.html', {
        "newyear": now.date == 1 and now.month == 1,
    })