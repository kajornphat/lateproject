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

def vote(request):
    if request.POST.get("vote_yes"):
        vote = request.POST.get("vote_yes")
        print(vote)
        print("perform voteYes")
        selected_question = Question.objects.get(id=vote)
        a = selected_question.say_yes + 1
        selected_question.say_yes = a
        selected_question.save()
        return render(request, 'result.html', {'num_voteyes' : selected_question.say_yes, 'num_voteno' : selected_question.say_no})
    
    if request.POST.get("vote_no"):
        vote = request.POST.get("vote_no")
        selected_question = Question.objects.get(id=vote)
        print(vote)
        print("perform voteNo")
        b = selected_question.say_no + 1
        selected_question.say_no = b
        selected_question.save()
        print("Number of vote no")
        print(selected_question.say_no)
        return render(request, 'result.html', {'num_voteyes' : selected_question.say_yes, 'num_voteno' : selected_question.say_no})    
    
    return redirect('/')
# def voteNo(request):
    

# Create your views here.
