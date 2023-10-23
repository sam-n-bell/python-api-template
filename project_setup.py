import os
import sys
import shutil
import logging
import stat

def check_for_new_directory(dir_name: str) -> str:
    os.chdir("..")
    directory = os.getcwd()
    new_dir = f"{directory}\\{dir_name}"
    exists = os.path.exists(new_dir)
    if exists:
        raise Exception(f"Directory {new_dir} already exists!")
    return new_dir


def copy_files(from_directory: str, to_directory: str):
    # copytree creates the new/to directory
    shutil.copytree(from_directory, to_directory)
    logging.info(f"files from {from_directory} copied to {to_directory}")
    files_to_del = ["project_setup.py", ".env", "name_replacer.sh", "README.md"]
    for file_name in files_to_del:
        try:
            path = os.path.join(to_directory, file_name)
            logging.debug(f"deleting {path}")
            os.chmod(path, stat.S_IWRITE)
            os.remove(path)
        except Exception as e:
            logging.error("removal_exception", file_name, str(e))


if __name__ == "__main__":
    current_directory = os.getcwd()
    project_name = sys.argv[1]
    if project_name is None:
        raise Exception("bad project name, try something else")
    new_directory = check_for_new_directory(project_name)
    copy_files(current_directory, new_directory)
