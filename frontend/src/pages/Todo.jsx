import "../App.css";
import { useEffect, useState } from "react";
import { TodoForm } from "../components/TodoForm";
import { TodoList } from "../components/TodoList";

import axios from "axios";

function Todo() {
  const [todos, setTodos] = useState([]);
  useEffect(() => {
    axios
      .get("http://localhost:8000/todos")
      .then((response) => {
        setTodos(response.data);
      })
      .catch((error) => {
        console.log("Failed getting todo list: ", error);
      });
  }, []);

  function addTodo(title) {
    const newTodo = {
      id: crypto.randomUUID(),
      title,
      completed: false,
    };

    setTodos((currentTodos) => [...currentTodos, newTodo]);

    axios.post("http://localhost:8000/todos/new", newTodo).catch((error) => {
      console.error("Failed adding todo: ", error);
    });
  }

  function toggleTodo(id, completed) {
    axios
      .put(`http://localhost:8000/todos/edit/${id}`, { completed })
      .then(() => {
        setTodos((currentTodos) =>
          currentTodos.map((todo) => {
            if (todo.id === id) {
              return { ...todo, completed };
            }
            return todo;
          })
        );
      })
      .catch((error) => {
        console.error("Failed updating todo: ", error.response);
      });
  }

  function deleteTodo(id) {
    axios
      .delete(`http://localhost:8000/todos/delete/${id}`)
      .then(() => {
        setTodos((currentTodos) =>
          currentTodos.filter((todo) => todo.id !== id)
        );
      })
      .catch((error) => {
        console.error("Failed deleting todo: ", error);
      });
  }

  return (
    <>
      <TodoForm addTodo={addTodo} />
      <TodoList todos={todos} toggleTodo={toggleTodo} deleteTodo={deleteTodo} />
    </>
  );
}

export default Todo;