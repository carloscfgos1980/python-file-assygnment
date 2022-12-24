
__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os
import zipfile
import os


def clean_cache():
    return os.mkdir('/Users/carlosinfante/Documents/Winc/files/cache')


print(clean_cache())


def cache_zip(zip_path, dir_path):
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(dir_path)


print(cache_zip('/Users/carlosinfante/Documents/Winc/files/data.zip',
                '/Users/carlosinfante/Documents/Winc/files/cache'))


def cached_files():
    arr = os.listdir('/Users/carlosinfante/Documents/Winc/files/cache')
    return arr


print(cached_files())


def find_password(source_location):
    search_string = 'password'
    passd = ''
    # list all the files in source location
    direct = os.listdir(source_location)

    # For loop to search for the string
    for file in direct:
        f = open(source_location + file, 'r')
        if search_string in f.read():
            print('file:', file)
            file_path = open(source_location + file, 'r')

            # Efficient way to search string in a large text file
            for l_no, line in enumerate(file_path):

                # search string
                if search_string in line:
                    print('string found in a file')
                    print('Line Number:', l_no)
                    print('Line:', line)
                    index_pass = line.find(':') + 2
                    passd = line[index_pass:]
    return passd


print('password is:', find_password(
    '/Users/carlosinfante/Documents/Winc/files/cache/'))
