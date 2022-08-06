#!/usr/bin/env python3
"""
Python console
"""

import cmd

class pyConsole(cmd.Cmd):
    """
    Python console
    """

    prompt = "$ "

    intro = "Hello there!! Welcome to Hbnb console, type help to list commands"
    
    def do_say_hi(self, person): 
        person = input("Tell us your name: ")
        if person:
            print("Hi,", person)
        else:
            print("Hello, John or Jane Doe")

    def help_say_hi(self):
        print('\n'.join(["Greets the named person.", "Otherwise greets a surprise person."]))

    def do_EOF(self, line):
        print("Bye bye!")
        return True

    def help_EOF(self):
        print("Closes the program safely. You can select 'Ctrl' + 'D' to achieve the same.")

if __name__ == '__main__':
    pyConsole().cmdloop()