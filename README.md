# FastAPI Task Manager — SQLite

A simple CRUD API built with **FastAPI** and **SQLite**.

This project started with tasks stored in an in-memory Python list. The storage layer was then replaced with SQLite while keeping the API endpoints and behavior essentially the same.

## What this project demonstrates

* FastAPI CRUD endpoints
* Pydantic request validation
* SQLite database integration
* SQL `SELECT`, `INSERT`, `UPDATE`, and `DELETE`
* Persistent data storage
* Automatic database and table creation
* Basic SQL exploration using SQLite

## Tech Stack

* Python
* FastAPI
* Pydantic
* SQLite
* Uvicorn
* uv

## API Endpoints

| Method | Endpoint           | Description               |
| ------ | ------------------ | ------------------------- |
| GET    | `/`                | Root endpoint             |
| GET    | `/root/options`    | Returns available options |
| GET    | `/tasks`           | Returns all tasks         |
| GET    | `/tasks/{task_id}` | Returns a task by ID      |
| POST   | `/tasks`           | Creates a new task        |
| PUT    | `/tasks/{task_id}` | Updates an existing task  |
| DELETE | `/tasks/{task_id}` | Deletes a task            |

## Database

SQLite was chosen because it is lightweight, requires no separate database server, and is easy to use for a small learning project.

The database is stored locally as:

```text
tasks.db
```

The database and `tasks` table are created automatically when the application is initialized.

The `tasks` table contains:

| Column  | Type    | Description                         |
| ------- | ------- | ----------------------------------- |
| `id`    | INTEGER | Primary key generated automatically |
| `title` | TEXT    | Task title                          |
| `done`  | BOOLEAN | Whether the task is completed       |

Three example tasks are inserted when the database is initialized for the first time.

## Running the Project

Clone the repository:

```bash
git clone <your-repository-url>
cd <project-folder>
```

Install dependencies:

```bash
uv sync
```

Start the development server:

```bash
uv run uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## Example SQL

I used SQLite directly to explore the database.

For example, to list all tasks:

```sql
SELECT * FROM tasks;
```

To show only completed tasks:

```sql
SELECT * FROM tasks WHERE done = 1;
```

To count the number of tasks:

```sql
SELECT COUNT(*) FROM tasks;
```

Changes made directly through SQL are reflected immediately when the API reads from the database.

## Database Screenshot

Screenshot of the `tasks` table opened in a SQLite database viewer:

> Add your DB Browser for SQLite screenshot here.

Example:

```text
![SQLite Database](./database-screenshot.png)
```

## Project Structure

```text
.
├── main.py
├── schemas.py
├── database.py
├── tasks.db
├── pyproject.toml
└── README.md
```

## Key Learning

The main goal of this project was to separate the **API layer** from the **data storage layer**.

The API endpoints remained the same while the underlying storage changed:

```text
Before:

FastAPI → Python list → Response


After:

FastAPI → SQL → SQLite → Response
```

This demonstrates how an API can maintain the same interface while changing its underlying data layer.
