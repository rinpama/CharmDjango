from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
def top(request):
    params={
        'title':'これは、M3ch　です。'
    }
    return render(request,'m3ch/top.html',params)