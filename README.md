# Python Todo CLI

A simple command-line todo list application built with Python. This application allows you to manage your tasks through an easy-to-use CLI interface, with data persistence using JSON storage.

## Features

- Add new tasks
- List all tasks with their completion status
- Data persistence using JSON storage

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

The application supports the following commands:

### Add a new task
```bash
python src/todo.py add "Your task description"
```

### List all tasks
```bash
python src/todo.py list
```

### Show help
```bash
python src/todo.py --help
```