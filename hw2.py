from typing import List, Tuple


to_do_list: List[Tuple[str, str]] = []


def add_task(task: str, priority: str) -> None:
    
    to_do_list.append((task, priority))


def show_tasks() -> None:
   
    print("Tasks:")
    for idx, (task, priority) in enumerate(to_do_list, start=1):
        print(f"{idx}. {task} - Priority: {priority}")


while True:
    task_input = input("Enter task (or type 'exit' to quit): ").strip()
    if task_input.lower() == 'exit':
        break
    priority_input = input("Enter priority (high/medium/low): ").strip()
    add_task(task_input, priority_input)
    show_tasks()
