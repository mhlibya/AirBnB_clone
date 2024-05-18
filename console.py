#!/usr/bin/python3

"""
Command interpreter module
Defines the command interpreter for the AirBnB clone project.
"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Command interpreter class for the AirBnB clone project."""

    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place, 'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}

    def do_create(self, args):
        """Create a new instance of BaseModel, save it, and print the id."""
        if not args:
            print("** class name missing **")
            return
        class_name = args.split()[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        instance = self.classes[class_name]()
        instance.save()
        print(instance.id)

    def do_show(self, args):
        """Print the string representation of an instance based on class name and id."""
        arg_list = shlex.split(args)
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        if arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        instance_key = f"{arg_list[0]}.{arg_list[1]}"
        if instance_key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[instance_key])

    def do_destroy(self, args):
        """Delete an instance based on the class name and id."""
        arg_list = shlex.split(args)
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        if arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        instance_key = f"{arg_list[0]}.{arg_list[1]}"
        if instance_key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[instance_key]
        storage.save()

    def do_all(self, args):
        """Print all string representations of all instances based or not on the class name."""
        if args:
            if args not in self.classes:
                print("** class doesn't exist **")
                return
            instances = [str(instance) for key, instance in storage.all().items()
                         if key.startswith(args)]
        else:
            instances = [str(instance) for instance in storage.all().values()]
        print(instances)

    def do_update(self, args):
        """Update an instance based on the class name and id by adding or updating an attribute."""
        arg_list = shlex.split(args)
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        if arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        instance_key = f"{arg_list[0]}.{arg_list[1]}"
        if instance_key not in storage.all():
            print("** no instance found **")
            return
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return
        if len(arg_list) == 3:
            print("** value missing **")
            return

        instance = storage.all()[instance_key]
        attribute_name = arg_list[2]
        attribute_value = arg_list[3]

        try:
            if '.' in attribute_value:
                attribute_value = float(attribute_value)
            else:
                attribute_value = int(attribute_value)
        except ValueError:
            pass  # It must be a string

        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

