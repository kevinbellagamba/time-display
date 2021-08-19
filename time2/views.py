from django.shortcuts import render
from time import gmtime, strftime

# Create your views here.
from django.shortcuts import render, HttpResponse
def index(request):
    context = {
        "time": strftime("%A, %B %dth %Y at %H:%M %p", gmtime())
    }
    return render(request,'index.html', context)

