from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answers = models.CharField(max_length=300)
    correct_answer = models.CharField(max_length=150)
    score = models.IntegerField(default=0)
    categories = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return self.question_text

    def separate(self):
        return self.answers.strip().split("|")
        


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    operate_score = models.IntegerField(default=0)
    programming_score = models.IntegerField(default=0)
    nummerical_score = models.IntegerField(default=0)
    architect_score = models.IntegerField(default=0)
    signals_score = models.IntegerField(default=0)
    networks_score = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.user.username} Profile'

    def get_total_score(self):
        return self.programming_score + self.operate_score + self.signals_score + self.networks_score + self.architect_score + self.nummerical_score

class Suggestion(models.Model):
    question_suggestion = models.CharField(max_length=100)
    answer = models.CharField(max_length=50)
    course = models.CharField(max_length=30)

    def __str__(self):
        return self.question_suggestion