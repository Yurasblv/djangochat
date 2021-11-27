from django.contrib.auth.models import User
from django.db import models

class Message(models.Model):
    text_message = models.TextField(max_length=1200, default='Text message')
    date = models.DateField(auto_now_add=True, blank=True)
    time = models.TimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.text_message}, {self.user}'

    class Meta:
        ordering = ('time',)
