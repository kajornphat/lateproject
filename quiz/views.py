from quiz.models import Question

from django.shortcuts import render, redirect
from django.http import HttpResponse

def home_page(request):
    first_question = Question.objects.all()
    return render(request, 'home_page.html', {'items' : first_question})

def addQuestion(request):
    if request.method == 'POST':
        new_question = request.POST['new_question']
        print(new_question)
        Question.objects.create( question_text= new_question)
        return redirect('/')
    return render(request, 'addQuestion.html')

# Create your views here.
