# Django notebook
## Git
### Git init
```
git init
git config --global user.name "Kirill Morozov"
git config --global user.email 157morozov@gmail.com
```
## Settings
### How to make superuser?
```
python manage.py createsuperuser
```
## Databases
### How to migrate apps?
```
python manage.py makemigrations app
python manage.py migrate app

# Maybe?
python manage.py migrate --run-syncdb 

```

