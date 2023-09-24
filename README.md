# Neural Dynamics Test Task

## Dependencies

- [docker](https://docs.docker.com/get-docker/)

## Api envinronment

- ### create `.env` file in `root` folder

#### `.env` example

```dosini
DEBUG=1
SECRET_KEY="django-insecure-44^#9_ar$$hy(*#+n@9fl-9cn+_4g=#7h)ak#%nk88vts(fdp0"
ALLOWED_HOSTS=web localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=webdb
SQL_USER=postgres
SQL_PASSWORD=admin
SQL_HOST=db
SQL_PORT=5432
```

- ### create `.db.env` file in `root` folder

#### `.db.env` example

```dosini
POSTGRES_USER=postgres
POSTGRES_PASSWORD=admin
POSTGRES_DB=webdb
```

## Build

```shell
docker-compose build
```

## Start

```shell
docker-compose up -d
```

## Note

### After starting the containers it will create superuser with credentials:

- username: `admin`
- email: `admin@example.com`
- password: `password`

## To generate entities

> Create users before products

### To generate users run

```shell
docker-compose exec web python manage.py generate_users <users_count (optional, default=100)>
```

### To generate products run

```shell
docker-compose exec web python manage.py generate_products <products_count (optional, default=100)>
```

## Django admin

```shell
http://localhost:8000/admin
```

## Note

### Current project uses custom package for django model admin [neural-admin](https://pypi.org/project/neural-admin/)
