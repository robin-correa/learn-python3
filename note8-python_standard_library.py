# [Working with Paths]

import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import webbrowser
import time
import json
from datetime import datetime
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

# path = Path("ecommerce")
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

# [Working with DateTimes]

dt1 = datetime(2018, 1, 1)
print(dt1)  # 2018-01-01 00:00:00
dt2 = datetime.now()
print(dt2)  # 2023-01-29 11:53:03.203512
# to tell python the specified date string to convert to object
dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
print(dt)

print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))

print(dt2 > dt1)  # True

print(time.time())  # total seconds since Jan 1970

# [Working with JSON Files]

movies = [
    {"id": 1, "title": "Terminator", "year": 1984},
    {"id": 3, "title": "Kindergarten Cop", "year": 1993},
]

# data = json.dumps(movies)
# Path('movies.json').write_text(data)

# Parse JSON from source
data = Path('movies.json').read_text()
movies = json.loads(data)
print(movies[0])  # {'id': 1, 'title': 'Terminator', 'year': 1984}

# [Opening the Browser]
# print("Deployment completed")
# webbrowser.open("https://www.linkedin.com/in/robin-correa-856010147/")

# [Sending emails]

# message = MIMEMultipart()
# message["from"] = "Robin Correa"
# message["to"] = "testuser@gmail.com"
# message["subject"] = "This is a test"
# message.attach(MIMEText("Body"))

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login("testuser@gmail.com", "testpassword")
#     smtp.send_message(message)
#     print("Sent...")

# [Command-line Arguments]

# Command: python .\note8-python_standard_library.py password21
if len(sys.argv) == 1:
    print("USAGE: python note8-python_standard_library.py <password>")
else:
    password = sys.argv[1]
    print("Password", password)  # Password password21
