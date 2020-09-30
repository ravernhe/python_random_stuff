#!/usr/bin/python
# -*-coding:utf-8 -*

import random
import re

regex_move = re.compile(r"^[zqsdlZQSDL]{1}$")

class Board:
    def __init__(self, height = 4, width = 4):
        self.board = []
        self.height = height
        self.width = width

    def create(self):
        self.board = [[0 for i in range (self.width)] for j in range (self.height)]
            
    def display(self):
        for i in range (0, self.height):
            print("{}\n".format(self.board[i]))
        print("\n")
    
class jeu(Board):
    def new_number(self):
        self.number = random.choice([2, 2, 2, 4])
    
    def get_new_number(self):
        x = random.randrange(0, self.width)
        y = random.randrange(0, self.height)
        while self.board[x][y] != 0:
            x = random.randrange(0, self.width)
            y = random.randrange(0, self.height)
        self.board[x][y] = self.number
            
    def can_move(self):
        movement = [0 for i in range (4)]
        for i in range (0, self.height):
            for j in range (self.width - 2, -1, -1):
                if self.board[i][j] != 0 and (self.board[i][j + 1] == 0 or self.board[i][j] == self.board[i][j + 1]):
                    movement[0] = 1
        for i in range (0, self.height):
            for j in range (1, self.width):
                if self.board[i][j] != 0 and (self.board[i][j - 1] == 0 or self.board[i][j] == self.board[i][j - 1]):
                    movement[1] = 1
        for i in range (1, self.height):
            for j in range (0, self.width):
                if self.board[i][j] != 0 and (self.board[i - 1][j] == 0 or self.board[i][j] == self.board[i - 1][j]):
                    movement[2] = 1
        for i in range (self.height  - 2, -1, -1):
            for j in range (0, self.width):
                if self.board[i][j] != 0 and (self.board[i + 1][j] == 0 or self.board[i][j] == self.board[i  + 1][j]):
                    movement[3] = 1
        return movement

    def move_right(self):
        for i in range (0, self.height):
            j = self.width - 2
            while j >= 0:
                token = 0
                if self.board[i][j] != 0 :
                    if self.board[i][j + 1] == 0 or self.board[i][j] == self.board[i][j + 1]:
                        token = 1
                    if self.board[i][j + 1] == 0:
                        self.board[i][j], self.board[i][j + 1] = 0, self.board[i][j]
                    elif self.board[i][j] == self.board[i][j + 1]:
                        self.board[i][j], self.board[i][j + 1] = 0, self.board[i][j + 1] * 2
                if token == 0:
                    j -= 1
                else:
                    j = self.width - 2
        return True

    def move_left(self):
        for i in range (0, self.height):
            j = 1
            while j < self.width:
                token = 0
                if self.board[i][j] != 0 :
                    if self.board[i][j - 1] == 0 or self.board[i][j] == self.board[i][j - 1]:
                        token = 1
                    if self.board[i][j - 1] == 0:
                        self.board[i][j], self.board[i][j - 1] = 0, self.board[i][j]
                    elif self.board[i][j] == self.board[i][j - 1]:
                        self.board[i][j], self.board[i][j - 1] = 0, self.board[i][j - 1] * 2
                if token == 0:
                    j += 1
                else:
                    j = 1
        return True

    def move_up(self):
        for j in range (0, self.width):
            i = 1
            while i < self.height:
                token = 0
                if self.board[i][j] != 0 :
                    if self.board[i - 1][j] == 0 or self.board[i][j] == self.board[i - 1][j]:
                        token = 1
                    if self.board[i - 1][j] == 0:
                        self.board[i][j], self.board[i - 1][j] = 0, self.board[i][j]
                    elif self.board[i][j] == self.board[i - 1][j]:
                        self.board[i][j], self.board[i - 1][j] = 0, self.board[i - 1][j] * 2
                if token == 0:
                    i += 1
                else:
                    i = 1
        return True
    
    def move_down(self):
        for j in range (0, self.width):
            i = self.width - 2
            while i >= 0:
                token = 0
                if self.board[i][j] != 0 :
                    if self.board[i + 1][j] == 0 or self.board[i][j] == self.board[i + 1][j]:
                        token = 1
                    if self.board[i + 1][j] == 0:
                        self.board[i][j], self.board[i + 1][j] = 0, self.board[i][j]
                    elif self.board[i][j] == self.board[i + 1][j]:
                        self.board[i][j], self.board[i + 1][j] = 0, self.board[i + 1][j] * 2
                if token == 0:
                    i -= 1
                else:
                    i = self.width - 2
        return True

    def make_move(self, possible_move):
        if self.move == 'd' and possible_move[0] == 1:
            return self.move_right()
        elif self.move == 'q' and possible_move[1] == 1:
            return self.move_left()
        elif self.move == 'z' and possible_move[2] == 1:
            return self.move_up()
        elif self.move == 's' and possible_move[3] == 1:
            return self.move_down()
        return False

    def get_move(self, possible_move):
        self.move = ""
        while not regex_move.match(self.move):
                self.move = input("Make a move : ")
        self.move = self.move.lower()
        if self.move == 'l':
            exit(0)
        return self.make_move(possible_move)

    def play(self):
        loose = False
        possible_move = []
        for i in range (2):
            self.new_number()
            self.get_new_number()
        self.display()
        print("Play with : 'z' 'q' 's' 'd' and press 'l' to quit.")
        while not loose == True:
            possible_move = self.can_move()
            if not 1 in possible_move:
                loose = True
            else :
                if self.get_move(possible_move) == True:
                    self.new_number()
                    self.get_new_number()
                    self.display()
        print("You loose.")