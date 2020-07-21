import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import enum
from enum import Enum
import pandas as pd
from walkermodule import Walker, Status
from boardmodule import Board

class Model:
    def __init__(self,board):
    #number of frames per second
    fps = 1000
        self.board = board
        self.symptom_chance = 0.01 #chance presymptomatic becomes infected
        self.recover_chance = 0.02 #chance asymptomatic recovers
        self.infected_probability = 0.5 #chance susceptible catches the virus
        self.infect_radius = 5
        self.uses_app_chance = 0.6 #adjust to change fraciton of app users
        #probabilities for transition from infected to each of the following three states
        self.incubate_prob = {Status.PRESYMPTOMATIC: 0.6, Status.ASYMPTOMATIC: 0.4}
        self.M = {Status.INFECTED: 0.99, Status.RECOVERED: 0.007, Status.DEAD: 0.003}
    def add_walker(self,status):
        #this command initialises an instance of the class Walker
        walker = Walker(x=np.random.randint(self.board.width),
                        y=np.random.randint(self.board.height),
                        status=status,
                        board=self.board,
                        model=self)
        #it then adds the generated walker to the list of walkers of the board that called the function
        self.board.walkers.append(walker)
