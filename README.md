# Django_Essential

## DO not push to main, create a branch and do a pull request when adding changes
## When you create a branch always make sure you branch off main, so that after the pull request we can merge it back to main
## Do not do large changes as this affects review quality
## When you create a PR (Pull Request) also take a short video showing the feature you added, so that everyone can quickly understand your Changes

### To run the server, use the following command:
```python3 manage.py runserver```

## Create an app
```django-admin startapp *AppName*```
## After adding a model on your app
### run this command to add the model to the database
```python3 manage.py makemigrations```
### run this command after makemigrations
```python3 manage.py migrate```

## Admin username and passwords
Username: admin
Password: admin

