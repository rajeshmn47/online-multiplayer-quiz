from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class questions(models.Model):
    question_text=models.CharField(max_length=100)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)

class score(models.Model):
    scores=models.IntegerField(unique=False)
    user=models.OneToOneField(User,on_delete=models.CASCADE)