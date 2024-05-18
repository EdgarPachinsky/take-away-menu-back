_Python version **3.11**_

_Django version **4.1.1**_

_Database **PSQL 15.2**_

## Run Local

* create virtual environment
```bash
python3 -m venv .venv
```
* install requirements for project
```bash
pip install -r requirements/local.txt
```

* Create DB
* Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## Run In Server

* create virtual environment
```bash
python3 -m venv .venv
```

* install requirements for project
```bash
pip install -r requirements/production.txt # or (dev, staging)
```

* handle static files
```bash
python manage.py collectstatic
```

* run with gunicorn
```bash
gunicorn take_away.wsgi
```