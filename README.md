# atena_api

Atena project

# Run

## Create a Virtual Env

```bash
python -m venv venv
```

## Activate the Virtual Env

```bash
source venv/bin/activate
```

## Install the requirements

```bash
pip install -r requirements.txt
```

## Start a mongodb on Docker

```bash
docker run \
-d \
--name atena_db \
-p 27017:27017 \
mongo
```


```dialect+driver://username:password@host:port/database```
