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
## YT guides
https://www.youtube.com/watch?v=6K83dgjkQNw
https://www.youtube.com/watch?v=EVrMbS14FdE&list=PLA0M1Bcd0w8xZA3Kl1fYmOH_MfLpiYMRs&index=8