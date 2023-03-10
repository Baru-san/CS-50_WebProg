from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, 'sumpahpemuda/index.html', {
        "sumpahpemuda" : now.month == 10 and now.day == 10
    })

    