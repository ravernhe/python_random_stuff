#!/usr/bin/python
# -*-coding:utf-8 -*

import random
import sys

arg = [sys.argv[1], sys.argv[2]]

class Argument:
    def __init__(self, arg):
        if self.check_arg(arg):
            self.arg1 = int(arg[0])
            self.arg2 = int(arg[1])
    
    def check_arg(self, arg):
        if len(sys.argv) != 3:
            self.quit("Usage : ./randomizer min max", 1)
        for a in range(len(arg)):
            if not arg[a].isnumeric():
                self.quit("[Min[{}] Max[{}]] invalid.".format(arg[0], arg[1]), 2)
        if arg[1] <= arg[0]:
            self.quit("Min[{}] Max[{}] invalid.".format(arg[0], arg[1]), 3)
        return True
    
    def quit(self, message, errno):
        print(message)
        exit(errno)

class Randomizer:
    def __init__(self, borne):
        self.minBorne = borne.arg1
        self.maxBorne = borne.arg2
    
    def go(self):
        print("Randomize : " + str(random.randint(self.minBorne, self.maxBorne)))



borne = Argument(arg)
rand = Randomizer(borne)
rand.go()