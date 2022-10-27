<hr />

## Development setup

<hr />

### Create python virutal enviroment

Create and active virtual enviroment using venv library:

```sh
python3 -m venv .venv
source .venv/bin/activate (Linux)
.venv\Scripts\activate (Windows)
```

In some Windows cases before activating venv:

```sh
Set-ExecutionPolicy Unrestricted -Scope Process
```

<hr />

### Setup flask app

Linux/MacOS

```sh
export FLASK_APP=flaskr/run.py
```

Windows cmd

```sh
set FLASK_APP=flaskr/run.py
```

Windows powershell

```sh
$env:FLASK_APP = "flaskr/run.py"
```

Install app as library in development mode using setuptool

```sh
python -m pip install -e .[dev]
```

Build package (run command each time after changes anmd before building image from Dockerfile)

```sh
python setup.py bdist_wheel
```

<hr />

### Run PosgreSQL database as container

```sh
docker run --name postgres_workshops -e POSTGRES_DB=dev_database -e POSTGRES_USER=dev_user -e POSTGRES_PASSWORD=dev_user -p 5432:5432 -d postgres:14
```

<hr />

### Run flask app

```sh
flask run
```

<hr />

### Run unit tests

```sh
pytest tests
```

<hr />

### Run linter

Pytlint

```sh
python -m pylint flaskr/** tests/**
```

Black check

```sh
python -m black --check .
```

Black fix

```sh
python -m black .
```
