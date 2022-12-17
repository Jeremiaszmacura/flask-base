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
export FLASK_DEBUG="True"
```

Windows cmd

```sh
set FLASK_APP=flaskr/run.py
set FLASK_DEBUG="True"
```

Windows powershell

```sh
$env:FLASK_APP="flaskr/run.py"
$env:FLASK_DEBUG="True"
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
docker run --name postgres_workshops -e POSTGRES_DB=dev_database -e POSTGRES_USER=dev_user -e POSTGRES_PASSWORD=dev_pass -p 5432:5432 -d postgres:14
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
python -m pylint flaskr tests
```

Black check

```sh
python -m black --check .
```

Black fix

```sh
python -m black .
```

<hr />

### Docker-compose

Start all containers

```sh
docker-compose up
```

Stop all containers

```sh
docker-compose down
```

<hr />

### Kubernetes

Apply k8 resources

```sh
kubectl apply -f .\postgres-config.yaml
kubectl apply -f .\postgres-secret.yaml
kubectl apply -f .\postgres.yaml
kubectl apply -f .\flask-app.yaml
```

Delete k8 resources

```sh
kubectl delete -f .\postgres-config.yaml
kubectl delete -f .\postgres-secret.yaml
kubectl delete -f .\postgres.yaml
kubectl delete -f .\flask-app.yaml
```

<hr />

### Build flask-app image

```sh
docker build -t flask-app:v1 .
```

<hr />

### URLs

App

```text
http://localhost:5000/
```