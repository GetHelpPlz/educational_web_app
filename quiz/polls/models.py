from django.db import models
from django_random_queryset import RandomManager

class Subject(models.Model):
    objects = RandomManager()
    subject_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.subject_text


class Question(models.Model):
    objects = RandomManager()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    answers = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text + self.answers

class Answer(models.Model):
    objects = RandomManager()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    def __str__(self):
        return self.answer_text
