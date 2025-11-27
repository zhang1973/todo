#import os
#script_dir = os.path.dirname(os.path.abspath(__file__))
#FILEPATH = os.path.join(script_dir, "todos.txt")
from pathlib import Path
FILEPATH = Path(__file__).resolve().parent/"todos.txt"
def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


