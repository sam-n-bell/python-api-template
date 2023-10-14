import os
import sys
import shutil


def check_for_new_directory(dir_name: str) -> str:
    os.chdir("..")
    directory = os.getcwd()
    new_dir = f"{directory}\\{dir_name}"
    exists = os.path.exists(new_dir)
    if exists:
        raise Exception(f"Directory {new_dir} already exists!")
    # os.makedirs(new_dir)
    # print(f"Python making directory {new_dir}")
    return new_dir


def copy_files(from_directory: str, to_directory: str):
    # copytree creates the new/to directory
    shutil.copytree(from_directory, to_directory)
    print(f"files from {from_directory} copied to {to_directory}")
    remove_file = os.path.basename(__file__)
    path = os.path.join(to_directory, remove_file)
    os.remove(path)


if __name__ == "__main__":
    current_directory = os.getcwd()
    project_name = sys.argv[1]
    # project_name = input("What do you want to call your project (ex: myproj-api)? ").strip()
    if project_name is None:
        raise Exception("bad project name, try something else")
    new_directory = check_for_new_directory(project_name)
    copy_files(current_directory, new_directory)
