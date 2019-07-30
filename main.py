#!python3
import string
import re
import command
from spellchecker import SpellChecker

def read_sentence():
    print("@ ", end="")
    raw_command = input().strip().split(" ")
    command = [re.sub(r'\W+', '', i).lower() for i in raw_command]
    spell = SpellChecker()
    spell_command = []
    for i in command:
        spell_command.extend(spell.candidates(i))
    return (command, raw_command, spell_command)

sentence, raw_command, spell_command = read_sentence()
while not 'exit' in sentence:
    pertaining_commands = [i for i in command.available_commands if i.pertains(sentence, raw_command, spell_command)]
    len(pertaining_commands) > 0 and pertaining_commands[0].run(sentence, raw_command, spell_command) # Make this more sophisticated
    sentence, raw_command, spell_command = read_sentence();
