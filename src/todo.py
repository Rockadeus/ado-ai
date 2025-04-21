#!/usr/bin/env python3
import argparse
import json
import os
from datetime import datetime
from pathlib import Path

TASKS_FILE = Path(__file__).parent.parent / "tasks.json"

def load_tasks():
    if TASKS_FILE.exists():
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(args):
    tasks = load_tasks()
    new_task = {
        'id': len(tasks) + 1,
        'title': args.title,
        'created_at': datetime.now().isoformat(),
        'completed': False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Added task: {new_task['title']}")

def list_tasks(args):
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    
    print("\nTODO List:")
    print("-" * 50)
    for task in tasks:
        status = "✓" if task['completed'] else " "
        print(f"[{status}] {task['id']}. {task['title']}")
    print("-" * 50)

def main():
    parser = argparse.ArgumentParser(description='Simple TODO list CLI application')
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Add task command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('title', help='Title of the task')
    
    # List tasks command
    list_parser = subparsers.add_parser('list', help='List all tasks')
    
    args = parser.parse_args()
    
    if args.command == 'add':
        add_task(args)
    elif args.command == 'list':
        list_tasks(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()