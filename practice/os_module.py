import os
from datetime import datetime

# print(os.getcwd())

a = os.chdir('C:/Users/Sarthak/Desktop/from_code/hello')
# print(os.getcwd())

# print(os.listdir())

# for making a single level directory(ps: code 14 level wont work since its prior level has not been created in 
# case of using this mkdir)
# os.mkdir('from_code')

# os.rmdir('from_code')

#  for making intermediate(tree) levels of directory(BETTER THAN MKDIR)
# for i in range(10):
#     os.makedirs('from_code/hello')

# NOT PREFERABLE, DELETES WHOLE DIRECTORY INCLUDED
# os.removedirs('from_code/hello')

# os.rename('from_code', 'to_code')

# ctime = create, atime = access , mtime = modified 
# mod_time = os.stat('The Witcher 3 - Wild Hunt.lnk').st_mtime

# print(datetime.fromtimestamp(mod_time))

# for dirpath, dirnames, filenames in os.walk('D:\Web Series'):  
#     print('Current Path:', dirpath)
#     print('Directories', dirnames)
#     print('Files', filenames)
#     print()

# print(os.environ.get('HOME'))

# file_path = os.path.join(a, 'test.txt')

## test path that does not exists
# print(os.path.dirname('/tmp/test.txt'))

# print(os.path.split('/tmp/test.txt'))

# print(os.path.exists('/tmp/test.txt'))

# print(os.path.isdir('/tmp/test.txt'))

# print(os.path.isfile('/tmp/test.txt'))

# print(os.path.splitext('/tmp/test.txt'))

