# Portfolio-API BACKEND
Project uses Django as a main Python web-framework and PostgreSQL as a database engine.   

## Project stack:
1. Python \>= 3.9 & pip
2. Django \>= 4.0.2
3. psycopg2 \>= 2.9.3

## Installation

#### Install dependencies
>Make sure you've installed pipenv

```pipenv install --dev``` for development mode  
```pipenv install``` for production mode

#### Configuring for development mode

```
sudo su postgres
psql
create database 'database_name'
\q
exit
cp .env.template .env
```
Fill each row in .env file with your data

### Running

```./manage.py runserver``` for production mode  
```sh ./start_dev_server.sh``` for development mode
