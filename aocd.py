import os
import requests


URL_TEMPLATE = "https://adventofcode.com/{}/day/{}/input"

def get_input(year, day):
    url = URL_TEMPLATE.format(year, day)
    session = os.environ.get("AOCD_SESSION")
    response = requests.get(url, cookies={"session": session})
    return response.text.splitlines()

