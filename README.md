# online_store

Привет, первым делом вам нужно скопировать репозиторий.
* Скопировать репозиторий:
```
git clone https://github.com/AktanKasymaliev/online_store.git
```
* Скачать виртульное окружени:
```
pip install python3-venv 
python3 -m venv venv
Aктивация: python3 -m venv venv
```
* Установить все зависимости: 
```
pip install -r requirements.txt
```

* Создать файл .env на уровне самого проекта, скопировать строки ниже, и подставить свои значения
```
SECRET_KEY = 
DEBUG = 
DB_PASSWORD = 
DB_USER = 
DB_NAME = 
EMAIL_HOST_USER = 
EMAIL_HOST_PASSWORD = 
```

* Этот проект был сделан на Postgresql, так что устанавливаем бд:
```
sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev postgres postgres-contrib (MacOS) / 
sudo apt-get install postgresql postgresql-contrib (Ubuntu)
sudo su - postgres(MacOS) /
sudo -u postgres psql
```
* Зайдите в Postgresql:
```
sudo -u postgres psql
CREATE DATABASE <database name>;
CREATE USER <database user> WITH PASSWORD 'your_super_secret_password';
ALTER ROLE <database user> SET client_encoding TO 'utf8';
ALTER ROLE <database user> SET default_transaction_isolation TO 'read committed';
ALTER ROLE <database user> SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE <database name> TO '<database user>';
```

* Синхронизируйте django с базой данных
```
- python manage.py makemigrations
- python manage.py migrate
```

* Create superuser
```
- python manage.py createsuperuser
```


* Наконец запустите сервер: `python3 manage.py runserver`
