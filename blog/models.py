from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# What we want to save in the database, Django already have a user model included

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if user is deleted, there post will also be deleted

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk}) #reverse to the detail page



