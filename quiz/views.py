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

def voteYes(request):
    vote = request.POST['Yes']
    selected_question = Question.objects.get(id=vote)
    a = selected_question.say_yes + 1
    selected_question.say_yes = a
    selected_question.save()
    return redirect('/')
        
def voteNo(request):
    vote = request.POST['No']
    selected_question = Question.objects.get(id=vote)
    b = selected_question.say_yes + 1
    selected_question.say_yes = b
    selected_question.save()
    return redirect('/')

# Create your views here.
