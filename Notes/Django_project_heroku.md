# Deploy Django Project On Heroku

### 1. Create django project : `django-admin startproject myproject`

### 2. Test local-server : `python manage.py runserver`

### 3. Login to heroku : `heroku login`

### 4. Initialise django project to git : `git init`
```
git add .
git commit -m 'first commit'
```

### 5. Create heroku app : `heroku create <app name optional>`

### 6. Add app name to project : `heroku git:remote <app_name>`

### 7. Install gunicorn : `pip install gunicorn`

### 8. Check from gunicorn server : `gunicorn myproject.wsgi`
	- if error occurs, add that host name to settings.py (`0.0.0.0`)
	- Here myproject is PROJECT_NAME

### 9. Make Procfile : `touch Procfile`
	- Add same command as local : web: gunicorn myproject.wsgi
	- here myproject is PROJECT_NAME

### 10. Test local heroku server : `heroku local`

### 11. Create requirementstxt : `pip freeze > requirements.txt`

### 12. Add heroku host name to settings.py : `<app_name>.herokuapp.com`

### 13. Stage changes and commit the changes and fire :
	git push heroku master