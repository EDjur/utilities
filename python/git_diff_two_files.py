import os
import subprocess
import pathlib

# Set these up depending on your usage
old_folder_path = os.path.join(os.getcwd(), "temp/folder_1")
new_folder_path = os.path.join(os.getcwd(), "folder_2")
diff_folder = "git_diff"
unwanted_folders = ['some_folder_name_i_dont_want']
unwanted_extensions = ('.pyc', '.DS_Store', '__init__.py')  # str.endswith() accepts a string or tuple

pathlib.Path(diff_folder).mkdir(parents=True, exist_ok=True)
out_path = os.path.join(os.getcwd(), diff_folder)


def create_diff_files():
    """
    Creates git .diff files for files in two identical file structures
    Useful for comparing all files of two exact copies of the same repo (i.e. same files, same folder structure)
    Outputs the .diff files in {out_path}, with the same folder structure as before
    Note: only works if you have two exact copies of the same folder structure and files as there is no matching logic
    """
    for (root_1, _, files_1), (root_2, _, files_2) in zip(os.walk(old_folder_path), os.walk(new_folder_path)):

        # Skip unwanted folders. root_1 should be same root_2. Therefore don't need to check (kind of)
        # Note this also removes substring-folders e.g. folder/folder_i_dont_want/folder_i_actually_want
        # So be careful!
        if any(unwanted in root_1 for unwanted in unwanted_folders):
            continue

        root_name = "/".join(root_1.split('/', maxsplit=6)[6:])

        # Remove any unwanted files depending on extension
        files_1 = [file for file in files_1 if not file.endswith(unwanted_extensions)]
        files_2 = [file for file in files_2 if not file.endswith(unwanted_extensions)]

        for file1, file2 in zip(files_1, files_2):
            if file1 != file2:
                print(f"Filenames not the same, skipping...: {file1} != {file2}")
                continue

            filename = os.path.join(diff_folder, root_name, f"{file1}.diff")
            full_file1_path = os.path.join(root_1, file1)
            full_file2_path = os.path.join(root_2, file2)

            pathlib.Path(os.path.dirname(filename)).mkdir(parents=True, exist_ok=True)  # Create directory for diff file

            # Create shell command
            cmd = f"git diff --no-index {full_file1_path} {full_file2_path} > {filename}"
            subprocess.run(cmd, shell=True)


if __name__ == '__main__':
    create_diff_files()
