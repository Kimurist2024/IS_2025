

from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.question.text} - {self.choice.text}"

class Community(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.TextField(help_text="カンマ区切りでタグを入力してください。例: インドア派,はい")

    def __str__(self):
        return self.name
