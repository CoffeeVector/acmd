#!/usr/bin/python3
import string
import re
import command

def read_sentence():
    print("@ ", end="")
    return [re.sub(r'\W+', '', i).lower() for i in input().strip().split(" ")]

sentence = read_sentence()
while not 'exit' in sentence:
    pertaining_commands = [i for i in command.available_commands if i.pertains(sentence)]
    len(pertaining_commands) > 0 and pertaining_commands[0].run(sentence) # Make this more sophisticated
    sentence = read_sentence();
