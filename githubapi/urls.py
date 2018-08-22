from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path


app_name = 'githubapi'

urlpatterns = [
    url(r'login/$', auth_views.LoginView.as_view(template_name = 'githubapi/registration/login.html'), name = 'login'),
    url(r'logout/$', auth_views.LogoutView.as_view(), name = 'logout'),
    url(r'signup/$', views.SignUpView.as_view(), name = 'signup'),
    url(r'search_user/user_search/$', views.SearchUserView, name ='user_search'),
    url(r'search_user/user_notexist/$', views.UserNotExistView.as_view(), name = 'user_notexist'),
    path('search_user/<str:username>/repos', views.RepoListView, name='user_detail'),   #dynamic url for RepoListView
    path('search_user/<str:owner>/<str:repo_name>/commits', views.CommitView, name='user_commit'), #dynamic url for CommitView

]
