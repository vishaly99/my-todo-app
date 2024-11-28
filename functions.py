#FILEPATH="../file/todo.txt"
FILEPATH="C:/Users/VishalYennam/PycharmProjects/webapp_1/todo.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

def count(phrase):
    return phrase.count('.')