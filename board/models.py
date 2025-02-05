from django.db import models
from datetime import datetime

class Thread(models.Model):
    thread_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.thread_text

class Response(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    response_text = models.TextField()
    name_text = models.CharField(max_length=50)
    tweet_date = models.DateTimeField('date tweeted')

    def __str__(self):
        return self.response_text