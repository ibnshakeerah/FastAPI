from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.responses import   FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Indicates how the task should look like
class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

# List to store tasks
tasks: List[Task] = []

# Get all tasks
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

# Create a new task
@app.post("/tasks", response_model=List[Task])
def create_task(task: Task):
    # check if task with the same id already exists
    for current_task in tasks:
        if current_task.id == task.id:
            raise HTTPException(status_code=400, detail="Task with this ID already exists")
    # add the new task to the list
    tasks.append(task)
    return tasks

# Update an existing task
@app.put("/tasks/{task_id}", response_model= List[Task])
def update_task(task_id: int, updated_task: Task):
    for index, current_task in enumerate(tasks):
        if current_task.id == task_id:
          tasks[index] = update_task
          return update_task 
    raise HTTPException(status_code=404, detail="Task not found")

# Delete a task
@app.delete("/tasks/{task_id}", response_model= List[Task])
def delete_task(task_id: int):
    for index, current_task in enumerate(tasks):
        if current_task.id == task_id:
            del tasks[index]
            return tasks
        raise HTTPException(status_code=404, detail="Task not found")  

app.mount("/static", StaticFiles(directory="."), name="static")

# Serve the HTML interface
@app.get("/")
def get_interface():
    return FileResponse("index.html")