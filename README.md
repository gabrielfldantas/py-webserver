# Python Simple Webserver

Python Flask + Waitress MVC webserver that stores incoming requests in Postgres, with basic or token authentication.

It exposes 4 POSTs endpoints, all of them stores data:
- /booking
- /gps
- /relational_operational_info
- /relation

1 health endpoint, it returns db connection healthness:
- /health


## Features

- Basic and Token authentication method supported;
- Postgres database storage for income calls;
- Configurable through environment variables;
- Error handling;
- Health endpoint.

## Next steps
- Add tests
- Add logging
- Docker support
- IaC

## Requirements
- Check .python-version, pyproject.toml and uv.lock.

## Setup

1. Clone the repository
2. [Install uv](https://docs.astral.sh/uv/getting-started/installation/#installing-uv)
3. Navigate to the project folder
````bash
cd py-webserver
````

4. Configure your `.env` file:
```env
#Waitress settings
WAITRESS_HOST=0.0.0.0
WAITRESS_PORT=8080

#Auth Type (basic or token)
AUTH_METHOD=token

#Basic Auth
USER_AUTH=usr
PASS_AUTH=pss

#Token Auth
TOKEN_AUTH=abc-123

#DB info
DB_URL=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASS=changeme
DB_NAME=postgres
TABLE_NAME=data
DB_URI=postgresql://${DB_USER}:${DB_PASS}@${DB_URL}:${DB_PORT}/${DB_NAME}
```

5. Run with Waitress:
```bash
uv run run.py
```

6. Send a POST call
```bash
curl -X POST 'http://127.0.0.1:8080/booking' --header 'Content-Type: application/json' --data '{"hi": "hello"}'
```

7. If you have a Postgres available and connected, should return success
```json
{"message":"Data saved successfully"}
```

## Authentication

The API supports multiple authentication methods configurable via the `AUTH_METHOD` environment variable:

- `basic`: Username/password authentication
- `token`: API key in X-API-Key header