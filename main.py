
__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os
import shutil
import zipfile

# get the path in the current directory generically so it will always work
path = os.getcwd()
# add 'cache' at the end of the path
directory = "cache"
path_to_cache = os.path.join(path, directory)

path_to_zip = os.path.join(path, "data.zip")

CHECK_FOLDER = os.path.isdir('cache')


def clean_cache():
    if CHECK_FOLDER:
        shutil.rmtree(path_to_cache)
    os.mkdir(path_to_cache)
    print("Directory '% s' created" % directory)


def cache_zip(zip_path, dir_path):
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(dir_path)


def cached_files():
    arr = os.listdir(path_to_cache)
    return arr


def find_password(source_location):
    search_string = 'password'
    passd = ''
    # list all the files in source location
    direct = os.listdir(source_location)

    # For loop to search for the string
    for file in direct:
        path_to_file = os.path.join(source_location, file)
        f = open(path_to_file, 'r')
        if search_string in f.read():
            print('file:', file)
            file_path = open(path_to_file, 'r')

            # Efficient way to search string in a large text file
            for l_no, line in enumerate(file_path):

                # search string
                if search_string in line:
                    print('string found in a file')
                    print('Line Number:', l_no)
                    print('Line:', line)
                    passd = line.split(" ")[1]
    return passd


if __name__ == "main":
    print(path_to_cache)
    print(path_to_zip)
    print(CHECK_FOLDER)
    print(clean_cache())
    print(cache_zip(path_to_zip, path_to_cache))
    print(cached_files())
    print('password is:', find_password(path_to_cache))
