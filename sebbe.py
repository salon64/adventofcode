import requests
import os
import os.path
import datetime
from dotenv import load_dotenv
load_dotenv()


current_day = str(datetime.date.today().day)
current_year = str(datetime.date.today().year)
aoc_url = fr"https://adventofcode.com/{current_year}/day/{current_day}/input"

auth = {"session": os.environ.get("AOC_SESSION_KEY")}
print(auth)
todays_input = requests.get(aoc_url, cookies=auth).text

folder_path = f"{current_year}/day{current_day}"
problem_path = f"day{current_day}"

input_path = f"day_{current_day}_input.txt"

if not os.path.exists(current_year):
    os.mkdir(current_year)

if not os.path.exists(folder_path):
    os.mkdir(folder_path)

with open(f"{folder_path}/{input_path}", "w") as file:
    file.write(todays_input)

if not os.path.exists(f"{folder_path}/{problem_path}a.py"):
    with open(f"{folder_path}/{problem_path}a.py", "w") as file:
        file.write(f"with open('{folder_path}/{input_path}', 'r') as file:\n\tdata = file.read()")

if not os.path.exists(f"{folder_path}/{problem_path}b.py"):
    with open(f"{folder_path}/{problem_path}b.py", "w") as file:
        file.write(f"with open('{folder_path}/{input_path}', 'r') as file:\n\tdata = file.read()")

print("Success")