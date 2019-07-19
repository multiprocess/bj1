from django.http import HttpResponse
from djano.shortcuts import redirect

def index(request):
    return HttpResponse('ddf')

def redirect(request):
    return redirect('/index/')
