from fastapi import FastAPI, HTTPException, Depends
from typing import Optional, List, Dict
from pydantic import BaseModel
from uuid import UUID, uuid4
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
    "localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TodoItem(BaseModel):
    id: UUID
    title: str
    completed: bool = False
class UpdateTodo(BaseModel):
    id: Optional[UUID] = None
    title: Optional[str] = None
    completed: Optional[bool] = None

todos = {UUID('b74d47c8-ff93-42cd-b4c4-d3e8a2195e6c'): TodoItem(id=UUID('b74d47c8-ff93-42cd-b4c4-d3e8a2195e6c'), title='Do WADS homework', completed=True), 
     UUID('fa7c932b-97a3-4f7f-b0e4-12f8a8e4b0a7'): TodoItem(id=UUID('fa7c932b-97a3-4f7f-b0e4-12f8a8e4b0a7'), title='Do WADS project', completed=False),
     UUID('bd4e62f7-7a28-49c5-b6d9-86c184b7c3a9'): TodoItem(id=UUID('bd4e62f7-7a28-49c5-b6d9-86c184b7c3a9'), title='Do other WADS homework', completed=False)}
    
todos = {}
@app.get('/todos')
def get_all_todos():
    print(todos)
    return list(todos.values())

@app.get('/todos/{id}')
def get_todo(id: UUID):
    if id not in todos:
        return {"error":"Title doesn't exist"}
    return todos[id]

@app.post('/todos/new')
def post_todo(todo: TodoItem) -> dict:
    todos[todo.id] = todo
    return {
        "data": {"Todo successfuly added"}
    }

@app.put("/todos/edit/{id}")
async def update_todo(id: UUID, todo: UpdateTodo):
    if id not in todos:
        return {"error":"ID doesn't exist"}

    if todo.title != None:
        todos[id].title = todo.title
    if todo.completed != None:
        todos[id].completed = todo.completed
    
    return todos[id]

@app.delete("/todos/delete/{id}")
async def delete_todo(id: UUID):
    if id not in todos:
        return {"error":"ID doesn't exist"}
    del todos[id]
    return {"msg":"Todo item successfully deleted"}