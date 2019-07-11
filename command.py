from abc import ABC, abstractmethod
import requests

class Command:
    @abstractmethod
    def pertains(self, command):
        pass

    @abstractmethod
    def run(self, command):
        pass

class WeatherCommand(Command):
    def pertains(self, command):
        return 'weather' in command

    def run(self, command):
        if "c" in command or "celsius" in command:
            print(requests.get('https://wttr.in/?m&0').text)
        elif "f" in command or "fahrenheit" in command:
            print(requests.get('https://wttr.in/?u&0').text)
        else:
            print(requests.get('https://wttr.in/?m&0').text) # ha metric for the win

available_commands = [WeatherCommand()]
