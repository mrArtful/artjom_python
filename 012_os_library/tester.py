import os
import time
import stat

# print(dir(os))

# print(os.getcwd())

# os.chdir(r"012_os_library")

# # print(os.getcwd())
# # print(os.listdir(r"../"))

# # os.mkdir(r"new_folder/test1/test123")  # mkdir() creates only one folder

# os.makedirs(r"new1/new2/new3/new4")

# # os.rename("text.txt", "new1/new2/new3/new4/text.txt")


# time.sleep(5)


# # os.rmdir(r"new1/new2/new3/new4")
# os.removedirs(r"new1/new2/new3")


# stats = os.stat(r"012_os_library/text.txt")

# print(stats)

# information = os.walk("./")

# for dirpath, dirnames, filenames in information:
#     print('-' * 30)
#     print(f'Current path: {dirpath}')
#     print(f'Directories: {dirnames}')
#     print(f'Files: {filenames}')


# information = os.walk(r"012_os_library/new1")

# for dirpath, dirnames, filenames in information:
#     if filenames:
#         for file_name in filenames:
#             os.remove(f"{dirpath}/{file_name}")

# print(os.environ['HOMEPATH'] + "hello")
# file_path = os.path.join(r"C:\\", 'hello', 'hello.txt')
# print(file_path)


# print(os.path.basename('/somedir/new_folder/sample'))
# print(os.path.dirname('/new/sample'))
# print(os.path.split('/somedir/new_folder/sample.txt'))


# if not os.path.exists(r'012_os_library/new1'):
#     os.mkdir('012_os_library/new1')

# print(os.path.isfile("012_os_library/new1"))
# print(os.path.isdir("012_os_library/new2"))

# print(os.path.splitext('somedir/tester'))

entries = os.scandir()

for entry in entries:
    if entry.is_file():
        print(f"File: {entry.name} - Size: {entry.stat().st_size}")
    elif entry.is_dir():
        print(f"Directory: {entry.name}")
