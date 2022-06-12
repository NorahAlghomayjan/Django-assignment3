from django.shortcuts import render , redirect
from django.urls import reverse
from urllib.parse import urlencode


# Create your views here.

def index (request):
    return render(request,'index.html')



def results(request):
    print(request.method)
    print("--"*80)
    print(request.POST)
    print("--"*80)
    option1 = request.POST.get('location')
    option2 = request.POST.get('language')
    comment = request.POST.get('comment')
    print(option1,option2,comment)
    context = {
        "name": request.POST.get('name'),
        "Location" :option1,
        "Language": option2,
        "comment" : comment
    }
    return render (request,'result.html',context)