#!/usr/bin/python3
import requests

def read_command():
    print("@ ", end="")
    return input()

def weather(command):
    if "C" in command or "Celsius" in command:
        print(requests.get('https://wttr.in/?m').text)
    elif "F" in command or "Fahrenheit" in command:
        print(requests.get('https://wttr.in/?u').text)
    else:
        print(requests.get('https://wttr.in/?m').text) # ha metric for the win

command = read_command();
while (not command == "exit"):
    command = command.strip().split(" ")
    if "weather" in command:
        weather(command)
    else:
        print(command)
    command = read_command();
