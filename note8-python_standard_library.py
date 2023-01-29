# [Working with Paths]

from pathlib import Path

Path(r"C:\Program Files\Microsoft")  # prefix-r means raw string
Path("/usr/local/bin")
Path()  # root
path = Path("ecommerce/__init__.py")
print(path.exists())
path.is_file()
path.is_dir()
print(path.name)  # File name with extension
print(path.stem)  # File name without extension
print(path.suffix)  # .py
print(path.parent)  # ecommerce
path = path.with_name("file.txt")
print(path.absolute())

path = path.with_suffix(".test")  # change file extension to .test
print(path)  # ecommerce\file.test

# [Working Directories]

path = Path("ecommerce")
path.mkdir()
path.rmdir()
path.rename("ecommerce2")
