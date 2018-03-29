from quiz.models import Question

from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    first_question = Question.objects.first()
    return render(request, 'home_page.html', {'item' : first_question})

# Create your views here.
