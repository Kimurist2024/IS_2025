from django.db import models
from django.contrib.auth.models import User


# 1. アンケート関連モデル
class Question(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="choices"
    )
    text = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.question.text} - {self.text}"


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - Q{self.question.id}: {self.choice.text}"


# 2. コミュニティ情報
class Community(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.CharField(
        max_length=255, blank=True
    )  # 例: "インドア,アニメ,スポーツ"

    def __str__(self):
        return self.name


# 3. チャット機能
class ChatRoom(models.Model):
    name = models.CharField(max_length=100)
    community = models.ForeignKey(
        Community, on_delete=models.CASCADE, related_name="chatrooms"
    )

    def __str__(self):
        return f"{self.community.name} - {self.name}"


class Message(models.Model):
    room = models.ForeignKey(
        ChatRoom, on_delete=models.CASCADE, related_name="messages"
    )
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} @ {self.room.name}: {self.text[:30]}"
