from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    say_yes = models.IntegerField(default=0)
    say_no = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text
# Create your models here.
