from django.urls import path

from quiz import views

urlpatterns = [
    path('', views.home_page, name='homepage'),
    path('addQuestion', views.addQuestion, name='AddQuestion'),
    path('voteyes', views.voteYes, name='VoteYES'),
    path('voteno', views.voteNo, name='VoteNO')

]
