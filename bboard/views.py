from django.http import HttpResponse
from django.shortcuts import render

from .models import Bd


# Create your views here.
def index(requset):
    bbs = Bd.objects.order_by('-published')
    return render(requset, 'bboard/index.html', {'bbs': bbs})
