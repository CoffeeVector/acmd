import requests


class WeatherCommand:
    def pertains(self, command, raw_command, spell_command):
        return 'weather' in command or 'weather' in spell_command

    def confidence(self, command, raw_command, spell_command): 
        return float(max(5, command.count('weather')))/5

    def run(self, command, raw_command, spell_command):
        if os.popen('command -v curl') == "":
            print("Sorry, I don't know how to get stuff on the internet. (install curl on your unix system)")
            return
        if "c" in command or "celsius" in command or 'c' in spell_command or 'celsius' in spell_command:
            print(requests.get('https://wttr.in/?m&0').text)
        elif "f" in command or "fahrenheit" in command or "f" in spell_command or "fahrenheit" in spell_command:
            print(requests.get('https://wttr.in/?u&0').text)
        else:
            print(requests.get('https://wttr.in/?m&0').text)  # ha metric for the win


import os
import re


class MathCommand:
    def pertains(self, command, raw_command, spell_command):
        return 'calculate' in command or 'calculate' in spell_command

    def confidence(self, command, raw_command, spell_command):
        return float(max(5, command.count('calculate')))/5
    
    def run(self, command, raw_command, spell_command):
        if os.popen('command -v bc') == "":
            print("Sorry, I'm too stupid to do math (install bc on your unix system).")
            return
        printed = False
        for i in raw_command:
            if not re.search('[a-zA-Z]', i):
                printed = True
                print(os.popen('echo "' + i + '" | bc -l').read())
        if not printed:
            print("I don't know what to calculate...")


import urllib
import subprocess

from lxml import html


class GoogleCommand:
    def pertains(self, command, raw_command, spell_command):
        keywords = ['google', 'search']
        return any([i in command for i in keywords]) or any([i in spell_command for i in keywords])

    def confidence(self, command, raw_command, spell_command):
        return float(max(5, command.count('google') + command.count('search')))/5

    def run(self, command, raw_command, spell_command): 
        try:
            index_of_google = command.index('google')
        except:
            index_of_google = len(command)
        try:
            index_of_search = command.index('search')
        except:
            index_of_search = len(command)
        index_of_google = index_of_google if (index_of_google < index_of_search) else index_of_search
        search_query_list = [i for j, i in zip(range(0, len(raw_command)), raw_command) if j > index_of_google]
        search_query = ""
        for i in search_query_list:
            search_query = search_query + i + " "
        url = "https://www.google.com/search?q=" + urllib.parse.quote(search_query, safe='~()*!.\'')
        r = requests.get(url)
        page = html.fromstring(r.text)
        test = r.text
        links = ["https://google.com/" + link for link in page.xpath('//div[contains(@class, "jfp3ef")]/a/@href')]
        links = links + [url]
        subprocess.run(['google-chrome', '--new-window'] + links[:5])


class TodoCommand:
    def pertains(self, command, raw_command, spell_command):
        keywords = ['todo', 'work']
        return any([i in command for i in keywords]) or any([i in spell_command for i in keywords])

    def confidence(self, command, raw_command, spell_command):
        return float(max(5, command.count('todo') + command.count('work')))/5
    
    def run(self, command, raw_command, spell_command):
        if os.popen('command -v shuf').read() == "":
            print("Sorry, I'm too stupid to do random things (install shuf on your unix system).")
        filename = os.popen('ls ~/.todo | shuf | head -n 1').read()
        print(filename)
        os.popen('st -e vim ~/.todo/' + filename)

from imageDisplayer import show_image
from io import BytesIO
from PIL import Image

class ApodCommand:
    def pertains(self, command, raw_command, spell_command):
        keywords = ['apod', 'astronomy']
        return any([i in command for i in keywords]) or any([i in spell_command for i in keywords])\

    def confidence(self, command, raw_command, spell_command):
        return float(max(5, command.count('apod') + command.count('astronomy')))/5

    def run(self, command, raw_command, spell_command):
        url = requests.get("https://api.nasa.gov/planetary/apod?date=2018-08-04&hd=True&api_key=DEMO_KEY").json()["hdurl"]
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))

        # show_image is a command that shows a image in the terminal given a PIL Image object
        show_image(img)

available_commands = [WeatherCommand(), MathCommand(), GoogleCommand(), TodoCommand(), ApodCommand()]
