import lib_platform
import os

def enter_downloads_path():
    pass
    #downloads_folder_path = input()
    #print(downloads_folder_path)

download_dolder_path = "/home/emr/Downloads"

file_types = {
    'Images': ['.jpg', '.jpeg', '.png'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    'Documents': ['.pdf', '.docx', '.txt', '.pptx'],
    'Audio': ['.mp3', '.wav'],
    'Archives': ['.zip', '.tar', '.rar', '.gz'],
    'undefined' : []
    }

def check_if_folder_exists(download_dolder_path):
    for file in file_types.keys():
        path = os.path.join(download_dolder_path, file)
        if os.path.exists(path):
            print(f"folder already exists: {file}")
        else:
            try:
                os.mkdir(path)
            except PermissionError:
                print("need sudo permissions to create a folder")

check_if_folder_exists(download_dolder_path)

def move_files(download_dolder_path):
    for x in os.listdir(download_dolder_path):
        isfile_path = os.path.join(download_dolder_path,x)
        is_file = os.path.isfile(os.path.join(isfile_path))
        print(x)
        print(is_file)
        if is_file:
            ext = x.split(".")[-1]
            print(ext)
        print("----------------")

move_files(download_dolder_path)