from django.shortcuts import render
from .models import Question
from django.http import HttpResponse


# Create your views here.
def home(request):
    que=Question.objects.all()
    if que:
     HttpResponse(que)
    else:
     HttpResponse("No questions available")