from collections.abc import Callable
import os
from os.path import exists

def generate_file_name(index: int) -> str:
    return f"ex_{index:03}.py"


def create_file(file_name: str) -> None:
    print(f"create file {file_name}")
    #open(file_name, 'a').close()


def rename_file_factory(old_name: str, new_name: str) -> Callable[[], None]:
    def rename_file() -> None:
        #os.rename(old_name, new_name)
        print(f"{old_name} => {new_name}")
    
    return rename_file


def fix_file_name_collisions(index: int, file_name: str) -> None:
    def generate_rename_actions() -> list[Callable[[], None]]:
        action_list: list[Callable[[], None]] = []
        previous_name = file_name
        current_name = file_name
        current_index = index
        while exists(current_name):
            current_index += 1
            current_name = generate_file_name(current_index)
            action_list.append(rename_file_factory(previous_name, current_name))
            previous_name = current_name
        return action_list
    
    def execute_actions_in_reverse(actions: list[Callable[[], None]]):
        actions.reverse()
        for action in actions:
            action()

    actions = generate_rename_actions()
    execute_actions_in_reverse(actions)


def insert_exercise(index: int) -> None:
    file_name = generate_file_name(index)
    if exists(file_name):
        fix_file_name_collisions(index, file_name)
    create_file(file_name)

os.chdir(r"D:\Users\Amine\Prgm\Python\Python.Cours.PYT\Exercices\Corrections")
insert_exercise(7)
