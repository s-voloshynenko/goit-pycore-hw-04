import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)

FOLDER_INDENT = 4 # default indent for nested files and folders

current_dir = Path(".")
folder_to_iterate = sys.argv[1]

def walk_through_folder(folder: Path, spaces = 0) -> None:
    """
    Print the specified folder and its nested files.
    If a folder contains subfolders, it will recursively log the contents of those subfolders.
    """
    # print the current folder
    print(f"{Fore.BLUE}{" " * spaces}{folder.name}/")

    # set internal indent for files and the nested folders
    indent = FOLDER_INDENT + spaces

    try:
        for item in folder.iterdir():
            if item.is_file():
                print(f"{Fore.GREEN}{" " * indent}{item.name}")
            if item.is_dir():
                walk_through_folder(item, spaces=indent)
    except FileNotFoundError as e:
        print(f"Folder or path doesn't exist, details: {e}")
        return None

if __name__ == "__main__":
    if not folder_to_iterate:
        print("Folder to iterrate was not specified.")
        sys.exit(1)

    path_to_folder = current_dir.joinpath(folder_to_iterate)

    if not path_to_folder.exists():
        print("Specified folder doesn't exist.")
        sys.exit(1)

    walk_through_folder(path_to_folder)
