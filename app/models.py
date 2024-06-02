from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    answer_text=models.CharField(max_length=200)
    
    def __str__(self):
        return self.answer_text