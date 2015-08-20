#!/usr/bin/python
# -*- coding: UTF-8 -*
from colorama import Fore, Back, Style
def success():
    print Fore.GREEN + "✔ success"
def info():
	print Fore.BLUE + "ℹ info"
def warning():
	print Fore.YELLOW + "⚠ warning" 
def error():
	print Fore.RED + "✖ error"
