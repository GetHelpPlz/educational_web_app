from django.db import models


# Answers must be written out within 200 characters of text.
# An answer may be pulled randomly for any question as a false answer.
class Subject(models.Model):
    subject_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.subject_text


class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    answers = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text + self.answers

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    def __str__(self):
        return self.answer_text
