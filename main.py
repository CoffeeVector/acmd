#!/usr/bin/python3
import string
import re
import command

def read_sentence():
    print("@ ", end="")
    raw_command = input().strip().split(" ")
    return ([re.sub(r'\W+', '', i).lower() for i in raw_command], raw_command)

sentence, raw_command = read_sentence()
while not 'exit' in sentence:
    pertaining_commands = [i for i in command.available_commands if i.pertains(sentence, raw_command)]
    len(pertaining_commands) > 0 and pertaining_commands[0].run(sentence, raw_command) # Make this more sophisticated
    sentence, raw_command = read_sentence();
