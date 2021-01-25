import os
import sys
import requests
from collections import deque
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from colorama import Fore

dir_name = sys.argv[1]

if not os.path.exists(dir_name):
    os.mkdir(dir_name)


stack = deque()


def work_stack(st):
    st.pop()
    return st.pop()


def parser_web_page(url):
    r = requests.get('https://' + url, headers={'User-Agent': UserAgent().chrome})
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.get_text()


while True:
    user = input()

    if user == 'exit':
        break

    elif user == 'back':
        back = work_stack(stack)
        current_file = open(f'tb_tabs/{back}', 'r')
        print(current_file.read())
        current_file.close()

    elif user not in stack:
        try:
            parser_web_page(user)
        except Exception:
            print('Error: Incorrect URL')
        else:
            file_web = user[:user.rindex('.')]
            web_page = open(f'tb_tabs/{file_web}', 'w')
            web_page.write(Fore.BLUE + parser_web_page(user))
            web_page.close()
            stack.append(file_web)
            print(Fore.BLUE + parser_web_page(user))

    elif user in stack:
        f = open(f'tb_tabs/{user}', 'r')
        print(f.read())
        f.close()
