import sys
import os
import requests
from collections import deque
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init
init()

dir_name = sys.argv[1]

if not os.path.exists(dir_name):
    os.mkdir(dir_name)

history = deque()


def get_site_content(url):
    return requests.get(url).text


def save_site_content(data, path):
    history.append(path)
    with open(os.path.join(dir_name, path), "w", encoding="utf-8") as f:
        f.write(data)


def go_site(site):
    address = site if site.startswith("https://") else f"https://{site}"
    site_content = get_site_content(address)
    soup = BeautifulSoup(site_content, "html.parser")
    text_for_save = ""
    for x in soup.find_all(["p", "title", "h1", "h2", "h3", "h4", "h5", "h6", "a", "ul", "ol", "li"]):
        text = x.get_text()
        text_for_save += f"\n{text}"
        if x.name == "a":
            print(Fore.BLUE + text)
            print(Style.RESET_ALL)
        else:
            print(text)
    save_site_content(text_for_save, site)


def go_back():
    history.pop()
    with open(os.path.join(dir_name, history.pop()), 'r') as f:
        print(f.read())


while True:
    command = input()
    if command == "exit":
        break
    if command == "back":
        go_back()
    elif "." in command:
        go_site(command)
    else:
        print("Error: Incorrect URL")
