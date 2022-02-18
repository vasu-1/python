# Deploy Normal Site On Heroku :-

### 1. We need to first login to heroku `heroku login`

### 2. create app from cli or from gui `heroku create <app name optional>`

### 3. `heroku git:remote -a <APP_NAME>`

### 4. Do neccessary changes

```git
git add .
git commit -m "initial commit"
git push heroku master
```

### 5. It will deploy the app (`we need app.json files for normal website hosting`) i guess it is optional but not sure !
it is not needed but we can try both