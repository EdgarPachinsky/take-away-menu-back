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
pip install -r requirements.txt
```

* Create DB
* Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
