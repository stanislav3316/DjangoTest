import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def __unicode__(self):
        return self.question

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=1))


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def __unicode__(self):
        return self.choice_textsql


class Course(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Student(models.Model):
    learnSubj = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    family = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " " + self.family
