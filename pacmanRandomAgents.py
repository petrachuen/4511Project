# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

import random, util

from game import Agent
from pacman import GameState

class PacmanRandomAgent(Agent):
    """
    Agent for the pacman to move
    Pacman move on random
    """
    
    def getAction(self, gameState: GameState):
        legalMoves = gameState.getLegalActions()

        # Choose random actions
        chosenAct = random.choice(legalMoves)

        return chosenAct
