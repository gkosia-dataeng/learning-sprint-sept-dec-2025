'''
    Problem: I want to do easyly filesystem operations (check the path, create new file...)
    Solution: pathlib module
'''

from pathlib import Path


# module with format correct the path accorting to operating system
path = Path('/home/gkosia/my-repos/learning-sprint-sept-dec-2025/python/python_patterns/01_factory_classes.py')

print(path.parts) # get each part, last the is the filename 
print(path.stem)  # get the filename without extension
print(path.suffix)  # get the filename  extension



print(f"Get files based on pattern name {[file for file in path.parent.glob('*')]}")

for file in path.parent.iterdir():
    if file.is_file():
        print(f"Its a file: {file}")
    if file.is_dir():
        print(f"Its a dir: {file}")

# read file
with path.open() as f:
    print(f.readline())