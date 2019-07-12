import requests

class WeatherCommand:
    def pertains(self, command, raw_command):
        return 'weather' in command

    def run(self, command, raw_command):
        if os.popen('command -v curl') == "":
            print("Sorry, I don't know how to get stuff on the internet. (install curl on your unix system)")
            return
        if "c" in command or "celsius" in command:
            print(requests.get('https://wttr.in/?m&0').text)
        elif "f" in command or "fahrenheit" in command:
            print(requests.get('https://wttr.in/?u&0').text)
        else:
            print(requests.get('https://wttr.in/?m&0').text) # ha metric for the win

import os
import re
class MathCommand:
    def pertains(self, command, raw_command):
        return 'calculate' in command
    
    def run(self, command, raw_command):
        if os.popen('command -v bc') == "":
            print("Sorry, I'm to stupid to do math (install bc on your unix system).")
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
import sys

from lxml import html
class GoogleCommand:
    def pertains(self, command, raw_command):
        return 'google' in command

    def run(self, command, raw_command): 
        index_of_google = command.index('google') 
        search_query_list = [i for j, i in zip(range(0, len(raw_command)), raw_command) if j > index_of_google]
        search_query = ""
        for i in search_query_list:
            search_query = search_query + i + " "
        url = "https://www.google.com/search?q=" + urllib.parse.quote(search_query, safe='~()*!.\'')
        r = requests.get(url)
        page = html.fromstring(r.text)
        test = r.text
        links = ["https://google.com/" + link for link in page.xpath('//div[contains(@class, "jfp3ef")]/a/@href')]
        subprocess.run(['google-chrome', '--new-window'] + links[:5])

available_commands = [WeatherCommand(), MathCommand(), GoogleCommand()]
