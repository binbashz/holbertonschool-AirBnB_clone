#!/usr/bin/python3
"""
Console module for AirBnB clone project.
"""
import sys
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
            }


class HBNBCommand(cmd.Cmd):
    """
    Command-line interpreter for AirBnB clone.
    """
    prompt = "(hbnb) "


def do_quit(self, arg):
    """
        Quit command to exit the program
        """
    return True


def do_EOF(self, arg):
    """
        EOF command to exit the program
        """
    print()
    return True


def emptyline(self):
    """
        Do nothing on empty input line
        """
        pass

def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it, and print the id
        """
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

def do_show(self, arg):
        """
        Print the string representation of an instance based on the class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

def do_all(self, arg):
        """
        Print all string representations of instances based on the class name (if provided)
        """
        args = arg.split()
        objects = storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        elif args[0] in storage.classes:
            class_name = args[0]
            print([str(obj) for key, obj in objects.items() if key.startswith(class_name)])
        else:
            print("** class doesn't exist **")

def do_update(self, arg):
        """
        Update an instance based on the class name and id by adding or updating attribute
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    instance = storage.all()[key]
                    attribute_name = args[2]
                    attribute_value = args[3].strip('"')
                    setattr(instance, attribute_name, attribute_value)
                    instance.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
