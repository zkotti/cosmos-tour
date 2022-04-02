# This script takes you to any typing section from the guide.html file!
# So when you run the program just type in the command line the section,
# that you want to go. The program will forward you there automatically
# from your browser.

# CAUTION ! ! !
# In order for this script to work you need to type the section, that
# you want to go exactly as it is in the guide.html file ! ! !

# I run this code on Windows 11, so I am sorry if this does not work
# on macOs or Linux.

# For example:
# if you want to go to the Countries section, then type "Countries" etc.

# It may not work in all the sections, so I hope you can make it work !


import requests
from bs4 import BeautifulSoup
import webbrowser


def find_name(tag, i):
    if tag not in i:
        return ''  
    cont = 0
    for index, val in i:
        if len(tag) == 4:
            cont += 1 if val in ['n', 'a', 'm', 'e'] else cont == 0
            if cont == len(tag):
                pos_start = index + 3
                break
        else:
            cont += 1 if val in ['<', 'e', 'm', '>'] else 0
            if cont == len(tag) + 2:
                pos_start = index + 1
                break
    pos_end = 0
    for index, val in enumerate(i):
        if index >= pos_start:
            if len(tag) == 4 and '"' == val:
                pos_end = index - 1
            else:
                if '<' == val:
                    pos_end == index - 1
    html_parameter = ''
    for index, val in enumerate(i):
        if index in range(pos_start, pos_end +1):
            html_parameter += val
    return html_parameter


name = input('Type the name of the section, that you want to search: ')
url = 'https://e-panourgia.github.io/cosmos-tour/guide.html'

res_guide = requests.get(url)
soup_guide = BeautifulSoup(res_guide.text, 'html.parser')

h2 = soup_guide.find_all('h2')
# print(soup_guide)
for i in h2:
    if name in str(i):
        html_parameter = find_name('name', str(i))
        webbrowser.open_new('https://e-panourgia.github.io/cosmos-tour/guide.html#' + html_parameter)
