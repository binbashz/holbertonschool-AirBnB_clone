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
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def help_quit(self):
        """ Help message for quit command """

        print("Quit command to exit the program.")
        print()

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it, and print the id.
        """
        args_list = arg.split()
        if len(args_list) < 1:
            print("** class name missing **")
        elif args_list[0] in class_dict.keys():
            new_instance = class_dict[args_list[0]]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Show the string representation of an instance based
        on the class name and id.
        """
        args_list = arg.split()
        if len(args_list) < 1:
            print("** class name missing **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        elif args_list[0] not in class_dict.keys():
            print("** class doesn't exist **")
        else:
            key = args_list[0] + "." + args_list[1]
            if key in storage.all().keys():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Destroy an instance based on the class name and id.
        """
        args_list = arg.split()
        if len(args_list) < 1:
            print("** class name missing **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        elif args_list[0] not in class_dict.keys():
            print("** class doesn't exist **")
        else:
            key = args_list[0] + "." + args_list[1]
            if key in storage.all().keys():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Print string representation of all instances based on the class name.
        """
        args = arg.split()
        if args and args[0] not in class_dict.keys():
            print("** class doesn't exist **")
        else:
            instances = [str(instance) for instance in storage.all().values()]
            print(instances)

    def do_update(self, arg):
        """
        Update an instance based on the class name and id.
        """
        args_list = arg.split()
        if len(args_list) < 1:
            print("** class name missing **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        elif args_list[0] not in class_dict.keys():
            print("** class doesn't exist **")
        else:
            key = args_list[0] + "." + args_list[1]
            if key in storage.all().keys():
                if len(args_list) < 3:
                    print("** attribute name missing **")
                elif len(args_list) < 4:
                    print("** value missing **")
                else:
                    instance = storage.all()[key]
                    attr_name = args_list[2]
                    attr_value = args_list[3].strip('"')
                    if hasattr(instance, attr_name):
                        attr_type = type(getattr(instance, attr_name))
                        setattr(instance, attr_name, attr_type(attr_value))
                        storage.save()
                    else:
                        print("** attribute doesn't exist **")
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
