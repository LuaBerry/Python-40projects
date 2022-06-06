import itertools
import zipfile
import os

def unzip(passwd_char_pool, min_len, max_len, zipFile, dir):
    for len in range(min_len, max_len + 1):
        to_attempt = itertools.product(passwd_char_pool, repeat = len)
        for attempt in to_attempt:
            passwd = ''.join(attempt)
            print(passwd)
            try:
                zipFile.extractall(pwd=passwd.encode(), path=dir)
                print (f"Password is {passwd}.")
                return 1
            except:
                pass
    return 0


passwd_chars = "0123456789"#"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = dir_path + "\\Precious file.zip"
zFile = zipfile.ZipFile(file_path)
min_length = 1
max_length = 4

unzip_result = unzip(passwd_chars, min_length, max_length, zFile, dir_path)

if unzip_result:
    print("Unzip successful.")
else:
    print("Unzip failed, Try longer password or bigger character pool.")