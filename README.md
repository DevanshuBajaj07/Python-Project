# Python-Project

# Simple To-Do List Application (Python)

A beginner-friendly **command-line To-Do List** app written in Python.  
This project lets users **add**, **view**, and **store** their daily tasks in a text file (`todo.txt`).  
It’s a great introduction to working with **files**, **loops**, and **user input** in Python.

---

## Features

- Add new tasks to a to-do list  
- View all saved tasks  
- Data automatically saved in a local text file (`todo.txt`)  
- Runs continuously until the user chooses to exit  
- Uses file handling (`a+` mode) to read and write tasks  

---

## How It Works

1. The program runs an infinite loop until you type `exit`.  
2. You can choose between:
   - `add` → Add a new task  
   - `view` → Display all tasks  
   - `exit` → Quit the app  
3. All tasks are stored in a file named `todo.txt` in the same directory as the script.

---

## Example Output

```
Would you like to add a task or view tasks? (add/view/exit): add
Enter the task you want to add: Finish Python homework
Task "Finish Python homework" added.

Would you like to add a task or view tasks? (add/view/exit): view
Your tasks:
1. Finish Python homework

Would you like to add a task or view tasks? (add/view/exit): exit
Exiting the To-Do application.
```

---

## Code Overview

```python
file = open("todo.txt", "a+")
```
- Opens (or creates) the file in append-and-read mode.

```python
file.seek(0)
tasks = file.readlines()
```
- Moves to the start of the file and reads all saved tasks.

```python
for idx, task in enumerate(tasks, start=1):
    print(str(idx) + ". " + task.strip())
```
- Prints each task with a number for easier readability.

---

## File Structure

```
 ToDoApp/
├── todo.py         # Main Python script
└── todo.txt        # Stores all tasks
```

---

## Requirements

- Python 3.x  
- Any text editor or IDE (VS Code, PyCharm, etc.)

---

##  How to Run

1. Clone or download the repository  
   ```bash
   git clone https://github.com/<your-username>/Simple-ToDo-App.git
   cd Simple-ToDo-App
   ```
2. Run the script  
   ```bash
   python todo.py
   ```

---

##  Future Improvements

- Add an option to delete completed tasks  
- Include timestamps or due dates  
- Create a GUI using `tkinter` or `PyQt`  
- Add task categories or priorities  

---

##  License

This project is licensed under the **MIT License** – feel free to use and modify it.
