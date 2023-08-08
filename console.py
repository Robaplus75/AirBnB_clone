#!/usr/bin/python3
"""
Command prompt entry point
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    command prompt entry point
    """
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """Exit on Ctrl-D"""
        return True
    
    def do_quit(self, line):
        """Quit the console"""
        return True
    
    def emptyline(self):
        """Repeat the last command"""
        return True



if __name__ == '__main__':
    HBNBCommand().cmdloop()