# StackOverFlow clone

this is a clone of StackOverFlow <br>

> license: [Beer]()

> created with [django-cookiecuuter](https://github.com/AbolfazlKameli/django-cookiecutter) for example.

## Features

- **JWT Authentication**: Secure API access with JSON Web Tokens.
- **DRF Spectacular**: Automatic OpenAPI/Swagger documentation generation.
- **PostgreSQL Database**: Robust relational database management system.
  
- **Redis for Caching**: High-performance cache layer for optimized API responses.
  
- **Redis as Celery Message Broker**: Redis is used as the message broker to efficiently handle task queues in Celery.
- **Arvan Cloud Storage Integration**: Efficient and scalable storage solution.
- **Celery**: Asynchronous task management for handling background processes.
- **Custom User Model**: Flexible user authentication system with extended functionality.
- **Two-Step Registration**: Includes user registration flow with an activation URL sent via email.
- **SMTP Configuration**: Pre-configured for sending emails, supporting various SMTP services.

## Authors

- [Abolfazl Kameli](https://github.com/AbolfazlKameli) (Backe-end dev)

## Run Locally

- Install required packages

visit Redis [installation guide](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/).

- Clone the project

```shell
$ git clone https://github.com/AbolfazlKameli/created-by-django-cookiecutter.git
```

- Go to the project directory

```shell
$ cd stackoverflow_clone
```

- Make a virtual environment

```shell
$ python3 -m venv .venv
```

- Activate virtual environment

```shell
$ source .venv/bin/activate 
```

- Install requirements

```shell
$ pip install -r requirements.txt
```

- Create Your `.env` file

```shell
$ cp .env.example .env
```

- Apply Migrations to the Database

```shell
$ python manage.py migrate
```

- Start the django server

```shell
$ python manage.py runserver
```

## Basic Commands

### Setting Up Your Users

To create a **superuser account**, use this command:
```shell
$ python manage.py createsuperuser
```

### Celery

This app comes with Celery.<br>
To run a celery worker:

```shell
$ celery -A core worker -l INFO
```

Please note: For Celery's import magic to work, it is important _where_ the celery commands are run. If you are in the
same folder with _manage.py_, you should be right.

### Tests

The users app comes with 68 test.<br>
To run tests:

```shell
$ python manage.py test
```

The tests are written for the pre-built users app in the stackoverflow_clone project.

## How this project created
this project created with [django-cookiecuuter](https://github.com/AbolfazlKameli/django-cookiecutter) as an example.
![terminal screeshot](https://github.com/AbolfazlKameli/created-by-django-cookiecutter/blob/main/terminal.png)


