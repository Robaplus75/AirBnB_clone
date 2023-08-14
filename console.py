#!/usr/bin/python3
"""
Command prompt entry point
"""

import cmd
import shlex
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage

myclasses = (
        "BaseModel", "City",
        "User", "State", "Place",
        "Amenity", "Review"
        )


def split(c_line: str):
    """
    For splitting the command line or string into tokens
    and returns the number of the tokens
    """
    args = shlex.split(c_line)
    return args, len(args)


class HBNBCommand(cmd.Cmd):
    """
    command prompt entry point
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exit on Ctrl-D"""
        return True

    def do_quit(self, line):
        """Quit the console"""
        return True

    def emptyline(self):
        """Repeat the last command"""
        pass

    def do_create(self, line):
        """
        For Creating a new instance of BaseModel
        saves it to the JSON file
        prints the id
        """
        args, arg_len = split(line)

        if arg_len == 0:
            print("** class name missing **")
        elif args[0] not in myclasses:
            print("** class doesn't exist **")
        elif arg_len == 1:
            obj = eval(args[0])()
            print(obj.id)
            obj.save()
        else:
            print("** Too many argument for create**")
            pass

    def do_show(self, line):
        """
        Prints the string represetnation of an instance
        based on the class name and id.
        """
        args, arg_len = split(line)
        objdict = storage.all()

        if arg_len == 0:
            print("** class name missing **")
        elif args[0] not in myclasses:
            print("** class doesn't exist **")
        elif arg_len == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, line):
        """
        For Deleting an instance
        based on the class name and id
        """
        args, arg_len = split(line)
        objdict = storage.all()

        if arg_len == 0:
            print("** class name missing **")
        elif args[0] not in myclasses:
            print("** class doesn't exist **")
        elif arg_len == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, line):
        """
        For printing all string representation of all instances
        based or not on the class name
        """
        args, arg_len = split(line)

        if arg_len > 0 and args[0] not in myclasses:
            print("** class doesn't exist **")
        else:
            my_objs = []
            for i in storage.all().values():
                if arg_len > 0 and args[0] == i.__class__.__name__:
                    my_objs.append(i.__str__())
                elif arg_len == 0:
                    my_objs.append(i.__str__())
            print(my_objs)

    def do_update(self, line):
        """
        For updating an  instance based on the class name and id
        by adding or updating attibute
        And saves the Changes to the JSON file
        """
        args, arg_len = split(line)
        objdict = storage.all()

        if arg_len == 0:
            print("** class name missing **")
            return False
        if args[0] not in myclasses:
            print("** class doesn't exist **")
            return False
        if arg_len == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if arg_len == 2:
            print("** attribute name missing **")
            return False
        if arg_len == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if arg_len == 4:
            myobj = objdict["{}.{}".format(args[0], args[1])]

            if args[2] in myobj.__class__.__dict__.keys():
                objtype = type(myobj.__class__.__dict__[args[2]])
                myobj.__dict__[args[2]] = objtype(args[3])
            else:
                myobj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            myobj = objdict["{}.{}".format(args[0], args[1])]

            for key, value in eval(args[2]).items():
                if (key in myobj.__class__.__dict__.keys() and
                        type(myobj.__class__.__dict__[key]) in {
                            int, float, str
                            }):
                    objtype = type(myobj.__class__.__dict__[key])
                    myobj.__dict__[key] = objtype(value)
                else:
                    myobj.__dict__[key] = value
        storage.save()
    
    def do_count(self, line):
        """Displays count of instance specified"""
        if line in myclasses:
            count = 0
            for key, val in storage.all().items():
                if line in key:
                    count +=1
            print(count)
        else:
            print("** class doesn't exist **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
