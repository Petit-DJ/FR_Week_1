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
    connection = get_connection()
    taskcreate = connection.execute(
        "INSERT INTO tasks (title, done) VALUES (?, ?)",
        (task.title, task.done)
    )
    connection.commit()
    connection.close()

    return  {"id": taskcreate.lastrowid, "title": task.title, "done": task.done}


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
    result = connection.execute(
        "UPDATE tasks SET title = ?, done = ? WHERE id = ?",
        (task.title, task.done, task_id)
    )
    if result.rowcount == 0:
        connection.close()
        raise HTTPException(status_code=404, detail="Task not found")

    connection.commit()
    connection.close()

    return { "id": task_id, "title": task.title, "done": task.done 
            }


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    connection = get_connection()
    result = connection.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    if result.rowcount == 0:
        connection.close()
        raise HTTPException(status_code=404, detail="Task not found")

    connection.commit()
    connection.close()

    return {"message": "Task deleted"}