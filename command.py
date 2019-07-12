import requests

class WeatherCommand:
    def pertains(self, command):
        return 'weather' in command

    def run(self, command):
        if "c" in command or "celsius" in command:
            print(requests.get('https://wttr.in/?m&0').text)
        elif "f" in command or "fahrenheit" in command:
            print(requests.get('https://wttr.in/?u&0').text)
        else:
            print(requests.get('https://wttr.in/?m&0').text) # ha metric for the win

import os
import re
class MathCommand:
    def pertains(self, command):
        return 'calculate' in command
    
    def run(self, command):
        printed = False
        for i in command:
            if not re.search('[a-zA-Z]', i):
                printed = True
                print(os.popen('echo ' + i + ' | bc -l').read())
        if not printed:
            print("I don't know what to calculate...")

available_commands = [WeatherCommand(), MathCommand()]
