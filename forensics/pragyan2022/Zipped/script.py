#!/usr/bin/python3
from os import system
import string
from string import *

a=ascii_uppercase
b=ascii_lowercase
system("cp Aa.zip .nvm.zip")
for i in a:
	for j in b:
		system(f'unzip {i+j}.zip ')
		system(f'rm {i+j}.zip')
