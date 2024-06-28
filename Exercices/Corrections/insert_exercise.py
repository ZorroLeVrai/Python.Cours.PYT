"""
Module utilisé pour insérer un fichier Python dans le répertoire de correction des exercices
"""

from collections.abc import Callable
import os
from os.path import exists


class FileHandler:
    """
    Classe pour la gestion des fichiers
    Attributes:
        execute_action : bool
            Si True effectue les opérations sur les fichiers sinon ne modifie pas les fichiers
    """

    def __init__(self, execute_action: bool):
        self.execute_action = execute_action

    def create_file(self, file_name: str) -> bool:
        print(f"create file {file_name}")
        if self.execute_action:
            try:
                with open(file_name, 'a'):
                    pass
            except OSError as os_error:
                print(os_error)
                return False
        return True

    def rename_file(self, old_name: str, new_name: str) -> bool:
        print(f"{old_name} => {new_name}")
        if self.execute_action:
            try:
                os.rename(old_name, new_name)
            except OSError as os_error:
                print(os_error)
                return False
        return True

    def file_exists(self, file_name: str) -> bool:
        """ Vérifie si le fichier file_name existe """
        return exists(file_name)


class ExerciseInsertor:
    """
    Classe permettant la création d'un fichier Python avec le bon index.
    Les autres fichiers sont décalés si besoin
    Attributes:
        file_handler : FileHandler
            prend en charge la gestion des fichiers
    """

    def __init__(self, file_handler: FileHandler, file_format: str):
        self.file_handler = file_handler
        self.file_format = file_format


    def generate_file_name(self, index: int) -> str:
        return self.file_format.format(index)

    def rename_file_factory(self, old_name: str, new_name: str) -> Callable[[], bool]:
        def rename_file() -> bool:
            return self.file_handler.rename_file(old_name, new_name)

        return rename_file

    def fix_file_name_collisions(self, index: int, file_name: str) -> bool:
        def generate_rename_actions() -> list[Callable[[], bool]]:
            action_list: list[Callable[[], bool]] = []
            previous_name = file_name
            current_name = file_name
            current_index = index
            while self.file_handler.file_exists(current_name):
                current_index += 1
                current_name = self.generate_file_name(current_index)
                action_list.append(self.rename_file_factory(previous_name, current_name))
                previous_name = current_name
            return action_list

        def execute_actions_in_reverse(actions: list[Callable[[], bool]]) -> bool:
            actions.reverse()
            for action in actions:
                is_action_done = action()
                if not is_action_done:
                    return False
            return True

        actions = generate_rename_actions()
        return execute_actions_in_reverse(actions)

    def insert_exercise(self, index: int) -> bool:
        file_name = self.generate_file_name(index)
        if self.file_handler.file_exists(file_name):
            is_collision_fixed = self.fix_file_name_collisions(index, file_name)
            if not is_collision_fixed:
                return False
        self.file_handler.create_file(file_name)
        return True


if __name__ == "__main__":
    os.chdir(r"D:\Users\Amine\Prgm\Python\Python.Cours.PYT\Exercices\Corrections")
    exerciceInsertor = ExerciseInsertor(FileHandler(False), "ex_{0:03}.py")
    exerciceInsertor.insert_exercise(7)
