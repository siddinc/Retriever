from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from . import forms
from githubapi.models import Search
from githubapi.forms import SearchForm
from django.views.generic import (View, TemplateView, DetailView, CreateView)
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import requests
import json


#class based views for login, logout, sign up, index, user_not_found templates
################################################################################

class ThanksPageView(TemplateView):
    template_name = 'githubapi/apptemplates/thanks.html'

class IndexView(TemplateView):
    template_name = 'githubapi/apptemplates/index.html'

class SignUpView(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'githubapi/registration/signup.html'

class UserNotExistView(LoginRequiredMixin, TemplateView):
    template_name = 'githubapi/apptemplates/user_notexist.html'

################################################################################


#function based views for user search, repo info, commit info templates
################################################################################

#view for searching github username or fullname
@login_required
def SearchUserView(request):
    #username gets saved in ModelForm
    form = SearchForm()
    if request.method == "POST":
        form = SearchForm(request.POST)

        if form.is_valid():
            s = form.save(commit=True)
            #url for getting user info response from github api
            url1 = 'https://api.github.com/search/users?q={}%20in:fullname&per_page=100'.format(s)
            json_data1 = requests.get(url1).json()

            if json_data1['total_count'] == 0:
                return render(request, 'githubapi/apptemplates/user_notexist.html', {})

            else:
                return render(request, 'githubapi/apptemplates/user_list.html', {"user_list": json_data1})

        else:
            print("Invalid Form!")

    return render(request, 'githubapi/apptemplates/user_search.html', {'form': form})

#view for displaying repo list of the searched user
@login_required
def RepoListView(request, username):
    #url for getting user info response from github api
    url2 = 'https://api.github.com/users/{}'.format(username)
    #url for getting repo info response from github api
    url3 = 'https://api.github.com/users/{}/repos'.format(username)
    json_data2 = requests.get(url2).json()
    json_data3 = requests.get(url3).json()

    return render(request, 'githubapi/apptemplates/user_detail.html', {"repo_data": json_data3, "user_data": json_data2})

#view for displaying commit history of the selected repo of the searched user
@login_required
def CommitView(request, owner, repo_name):
    #url for getting commit info response from github api
    url4 = 'https://api.github.com/repos/{a}/{b}/commits'.format(a = owner, b = repo_name)
    json_data4 = requests.get(url4).json()

    return render(request, 'githubapi/apptemplates/user_commit.html', {"commit_data": json_data4, "repo_name": repo_name})

################################################################################
