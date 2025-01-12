import lib_platform
import os
import shutil

def enter_downloads_path():
    pass
    #downloads_folder_path = input()
    #print(downloads_folder_path)

download_folder_path = "/home/emr/Downloads"

file_types = {
    "Images": ["jpg", "jpeg", "png"],
    "gif": ["gif"],
    "Videos": ["mp4", "avi", "mkv", "mov"],
    "Documents": ["pdf", "docx", "txt", "pptx"],
    "Audio": ["mp3", "wav"],
    "Archives": ["zip", "tar", "rar", "gz"],    }

def check_if_folders_exists(download_folder_path):
    for file in file_types.keys():
        path = os.path.join(download_folder_path, file)
        if os.path.exists(path):
            pass
            #print(f"folder already exists: {file}")
        else:
            try:
                os.mkdir(path)
            except PermissionError:
                print("need sudo permissions to create a folder")

def move_files(download_folder_path):
    i=0
    for x in os.listdir(download_folder_path):
        isfile_path = os.path.join(download_folder_path,x)
        is_file = os.path.isdir(os.path.join(isfile_path))
        
        if not is_file:
            ext = x.split(".")[-1]            

            for folder , extension in file_types.items():
                if ext in extension:
                    ext_dest = folder
                    final_dest = os.path.join(download_folder_path, folder, x)
                    shutil.move(isfile_path, final_dest)
                    i=i+1
                    print(f"{isfile_path} moved into {folder} : {final_dest}, moved file number : {i}")
                    print("-----------")

check_if_folders_exists(download_folder_path)
move_files(download_folder_path)