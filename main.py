from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List
from fastapi.responses import   HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
          return tasks
    raise HTTPException(status_code=404, detail="Task not found")

# Delete a task
@app.delete("/tasks/{task_id}", response_model= List[Task])
def delete_task(task_id: int):
    for index, current_task in enumerate(tasks):
        if current_task.id == task_id:
            del tasks[index]
            return tasks
    raise HTTPException(status_code=404, detail="Task not found")  

# CORS middelware to allow requests from the frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 templates for rendering HTML
templates = Jinja2Templates(directory="templates")

# Serve the HTML interface
@app.get("/", response_class=HTMLResponse)
def get_interface(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})