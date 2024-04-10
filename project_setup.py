import os
import sys
import shutil
import logging
import stat


def check_for_new_directory(dir_name: str, use_single_slash: bool) -> str:
    os.chdir("..")
    directory = os.getcwd()
    new_dir = f"{directory}\\{dir_name}" if not use_single_slash else f"{directory}/{dir_name}"
    exists = os.path.exists(new_dir)
    if exists:
        raise Exception(f'directory name {dir_name} taken! :bad: ')
    else:
        print(f'directory name {dir_name} not taken :good: ')
    return new_dir


def copy_files(from_directory: str, to_directory: str):
    # copytree creates the new/to directory
    shutil.copytree(from_directory, to_directory)
    logging.info(f"files from {from_directory} copied to {to_directory}")
    files_to_del = ["project_setup.py", "name_replacer.sh"]
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
    print(sys.argv)
    project_name = sys.argv[1]
    if project_name is None:
        raise Exception("bad project name, try something else")
    use_single_slash = sys.argv[2] and sys.argv[2] == '1'
    new_directory = check_for_new_directory(project_name, use_single_slash)
    copy_files(current_directory, new_directory)
