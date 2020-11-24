from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField()

    @property
    def short_info(self):
        return f'{self.author.username}, {self.created_date}'

    def __str__(self):
        return self.text
