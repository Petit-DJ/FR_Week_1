# Basic FastAPI API

A simple FastAPI project demonstrating the creation of basic REST API endpoints.

## Features

* GET and POST endpoints
* Path & query parameters
* Request body validation with Pydantic
* Automatic API documentation

## Installation

```bash
pip install fastapi uvicorn
```

## Run

```bash
uvicorn main:app --reload
```

The API will be available at:

* `http://127.0.0.1:8000`
* Swagger Docs: `http://127.0.0.1:8000/docs`
* ReDoc: `http://127.0.0.1:8000/redoc`

## Example Endpoints

| Method | Endpoint      | Description       |
| ------ | ------------- | ----------------- |
| GET    | `/items`      | Get all items     |
| GET    | `/items/{id}` | Get an item by ID |
| POST   | `/items`      | Create a new item |

## Tech Stack

* Python
* FastAPI
* Uvicorn
* Pydantic
