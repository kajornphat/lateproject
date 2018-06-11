from django.test import TestCase
from quiz.models import Question

# class HomepageTest(TestCase):

#     def test_bad_maths(self):
#         self.assertEqual(1+1, 3)

class addQuestionTest(TestCase):

    def test_addQuestion_can_save_a_POST_request(self):
        response = self.client.post('/addQuestion',
        {'new_question': 'THIS IS A NEW QUESTION?'})

        self.assertEqual(Question.objects.count(),1)
    
    def test_vote_the_question(self):
        response = self.client.post('/addQuestion',
        {'new_question': 'THIS IS A NEW QUESTION?'})
        a = Question.objects.first()
        self.assertEqual(a.question_text,'THIS IS A NEW QUESTION?')

        a.say_yes = 1 #vote count
        self.assertEqual(a.say_yes, 0)

# Create your tests here.
