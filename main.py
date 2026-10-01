# #main.py
from fastapi import FastAPI, HTTPException

from database import get_connection
from schemas import Task, TaskCreate

app = FastAPI()


tasks = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Build CRUD API", "done": False},
    {"id": 3, "title": "Learn SQLite", "done": False},
]


@app.get("/")
def get_root():
    return {"Message": "Hey sup!"}


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    new_id = max(item["id"] for item in tasks) + 1 if tasks else 1

    new_task = {
        "id": new_id,
        "title": task.title,
        "done": task.done
    }

    tasks.append(new_task)

    return new_task


@app.get("/tasks")
def get_tasks():
    connection = get_connection()
    tasks = connection.execute(
        "SELECT * FROM tasks"
    ).fetchall()
    connection.close()

    return [dict(task) for task in tasks]


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    connection = get_connection() # open the connection
    task = connection.execute(
        "SELECT * FROM tasks WHERE id = ?", (task_id,) #ggive sql command regarding endpoint
    ).fetchone()
    connection.close() #close the connection

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate):
    connection = get_connection()
    task = connection.execute(
        "SELECT * FROM tasks WHERE id = ?", (task_id)

    )

    for existing_task in tasks:
        if existing_task["id"] == task_id:
            existing_task["title"] = task.title
            existing_task["done"] = task.done

            return existing_task

    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    for existing_task in tasks:

        if existing_task["id"] == task_id:
            tasks.remove(existing_task)

            return {"message": "Task deleted"}

    raise HTTPException(status_code=404, detail="Task not found")
