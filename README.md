This is a simple Django 2.7 project that collects funny vines globally and puts then in one place.

.
Features

    Django 2.0+
    Uses Pipenv - the officially recommended Python packaging tool from Python.org.
    Development, Staging and Production settings with django-configurations.
    Collection of custom extensions with django-extensions.
    HTTPS and other security related settings on Staging and Production.
    Procfile for running gunicorn with New Relic's Python agent.
    PostgreSQL database support with psycopg2.
    Check the requirement.txt file for more

How to Use

Clone the project fom the following url https://github.com/ORC-1/vine.git
Install all dependecies using requirements file 
eg pip install -r requirements.txt
Set the .env.example to .env and fill accordingly
run the migrate command 
eg: python manage.py migrate
Creatersupeuser using the python manage.py createsuperuser command
login
go to newvid url to upload contents 
upolad contents and enjoy :-) 

Environment variables

These are common between environments. The ENVIRONMENT variable loads the correct settings, possible values are: DEVELOPMENT, STAGING, PRODUCTION.

ENVIRONMENT='DEVELOPMENT'
DJANGO_SECRET_KEY='dont-tell-eve'
DJANGO_DEBUG='yes'

These settings(and their default values) are only used on staging and production environments.

DJANGO_SESSION_COOKIE_SECURE='yes'
DJANGO_SECURE_BROWSER_XSS_FILTER='yes'
DJANGO_SECURE_CONTENT_TYPE_NOSNIFF='yes'
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS='yes'
DJANGO_SECURE_HSTS_SECONDS=31536000
DJANGO_SECURE_REDIRECT_EXEMPT=''
DJANGO_SECURE_SSL_HOST=''
DJANGO_SECURE_SSL_REDIRECT='yes'
DJANGO_SECURE_PROXY_SSL_HEADER='HTTP_X_FORWARDED_PROTO,https'

Deployment

It is possible to deploy to Heroku or to your own server.
Heroku

$ heroku create
$ heroku addons:add heroku-postgresql:hobby-dev
$ heroku addons:add newrelic
$ heroku pg:promote DATABASE_URL
$ heroku config:set ENVIRONMENT=PRODUCTION
$ heroku config:set DJANGO_SECRET_KEY=`./manage.py generate_secret_key`

License

The MIT License (MIT)

Copyright (c) 2012-2017 José Padilla

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.