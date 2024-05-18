#!/usr/bin/python3

import shlex
import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
	"""Command interpreter for HBNB"""

	classes = {"BaseModel": BaseModel}
	prompt = "(hbnb) "

	def do_creat(self, arg):
		"""Creates a new instance of BaseModel, saves it, and prints the id."""
		if not arg:
			print("** class name missing **")
			return
		class_name = shlex.split(arg)[0]
		if class_name not in self.classes:
			print("** class doesn't exist **")
			return
		instance = self.classes[class_name]
		instande.save()

	def do_show(self, args):
		"""Prints the string representation of an instance based on the class name and id."""
		args_list = shlex.split(args)
		if len(args_list) == 0:
			print("** class name missing **")
			return
		if len(args_list) == 1:
			print("** instance id missing **")
			return
		if args_list[0] not in self.classes:
			print("** class doesn't exist **")
			return
		key_args = "{}.{}".format(args_list[0], args_list[1])
		if key_args not in storage.all():
			print("** no instance found **")
			return
		print(FileStorage.all()[key_args])

	def do_destroy(self, args):
		"""Deletes an instance based on the class name and id."""
		rgs_list = shlex.split(args)
		if len(args_list) == 0:
                        print("** class name missing **")
                        return
		if len(args_list) == 1:
                        print("** instance id missing **")
                        return
		if args_list[0] not in self.classes:
                        print("** class doesn't exist **")
                        return
		key_args = "{}.{}".format(args_list[0], args_list[1])
		if key_args not in storage.all():
                        print("** no instance found **")
                        return
		del storage.all()[key_args]
		storage.save()

	def do_all(self, arg):
		"""Prints all string representation of all instances based or not on the class name."""
		args = shlex.spoit(arg)
		all_objs = storage.all()

		if len(args) < 1:
			print(["{}".format(str(v)) for _, v in all_objs.items()])
			return
		if args[0] not in current_classes.keys():
			print("** class doesn't exist **")
			return
		else:
			print(["{}".format(str(v))
				for _, v in all_objs.items() if type(v).__name__ == args[0]])
			return

	def do_update(self, args):
		"""Updates an instance based on the class name and id by adding or updating attribute."""
		args_list = shlex.split(args)
		if len(args_list) == 0:
			print("** class name missing **")
			return
		if args_list[0] not in self.classes:
			print("** class doesn't exist **")
			return
		if len(args_list) == 1:
			print("** instance id missing **")
			return
		key_args = "{}.{}".format(args_list[0], args_list[1])
		if key_args not in storage.all():
			print("** no instance found **")
			return
		if len(args_list) == 2:
			print("** attribute name missing **")
			return
		if len(args_list) == 3:
			print("** value missing **")
			return
		storage.all()[key_args][args_list[3]] = args_list[4]

	def do_quit(self, arg):
		"""Exit the program"""
		return True

	def do_EOF(self, art):
		"""Exit the program"""
		print("")
		return True

	def emptyline(self):
		"""Do nothing on empty line"""
		pass

if __name__ == "__main__":
	HBNBCommand().cmdloop()
