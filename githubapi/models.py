from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib import auth


class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return self.username

class Search(models.Model):
    github_username = models.CharField(max_length = 100, verbose_name = 'GitHub Username')

    def __str__(self):
        return self.github_username
