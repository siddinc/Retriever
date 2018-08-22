# RETRIEVER
----
- This is the first **DJ Unicode** task.
- Retriever is a website which uses the **GitHub REST API v3** to get the data queried by registered users.

## DEMO:
----
- http://siddinc.pythonanywhere.com
- username: xyz
- password: xyzxyzxyz

## SCREENSHOTS:
----
![desktop_user_search](/screenshots/desktop_user_search.png)
![mobile_index](/screenshots/mobile_index.png)
![mobile_login](/screenshots/mobile_login.png)
![mobile_user_search](/screenshots/mobile_user_search.png)
![desktop_user_detail](/screenshots/desktop_user_detail.png)

#### For more screenshots, refer to the screenshots folder.

## REQUIREMENTS BEFORE RUNNING SETUP:
----
- `pip install -r requirements.txt`
- `pip install django-bootstrap4`


## KEY FEATURES:
----
- `bcrypt` and `agron2` password hashing
- Custom  `User`  model
- Custom project structure (See below)


## PROJECT STRUCTURE:
----
- `static` folder contains `master.css`
- `githubapi` module contains the django app
- `templates/githubapi` contains the templates for frontend development
- `retriever` module is the original project folder that contains settings, root URLs,  and other WSGI