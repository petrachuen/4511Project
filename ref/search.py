# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py) .
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

class Node:
    def  __init__(self, s):
        #print(s)
        self.s = s
        if (len(s) == 3):
            #print("first case")
            self.state = s[0]
            self.dir = s[1]
            self.pc = s[2]
        else:
            self.state = s
            self.dir = s
            self.pc = 0
            #print()
        self.track = []
        self.cost =0
    
    def toString(self):
        return (self.s)
        

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    node  = Node(problem.getStartState())
    frontier = util.Stack()
    frontier.push(node)
    reach = []

    while (not frontier.isEmpty()):
        #print(node.track)
        node = frontier.pop()
        if (node.state != problem.getStartState()): # and (node.state not in reach):
            node.track.append(node.dir)
        
        if (problem.isGoalState(node.state)):
            #node.track.append(node.dir)
            return node.track
        
        elif (node.state not in reach):
            ChildList = problem.getSuccessors(node.state)
            for child in (ChildList):
                if(child not in reach):
                    cn = Node(child)
                    cn.track = cn.track + node.track
                    frontier.push(cn)

        
        reach.append(node.state)
    
    #return a list of actions that will lead agents from start to goal
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    node = Node(problem.getStartState())

    if (problem.isGoalState(node.state)):
        return node.track
    
    frontier = util.Queue()
    frontier.push(node)
    reach = []
    reach.append(problem.getStartState())

    while (not (frontier.isEmpty())):
        node = frontier.pop()
        if (node.state != problem.getStartState()): # and (node.state not in reach):
            node.track.append(node.dir)
        
        if (problem.isGoalState(node.state)):
                return node.track
        
        for child in (problem.getSuccessors(node.state)):
            cn = Node(child)
            if (cn.state not in reach):
                cn.track = cn.track + node.track
                reach.append(cn.state)
                frontier.push(cn)
    
    return []
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    node = Node(problem.getStartState())
    frontier = util.PriorityQueue() #by path cost
    frontier.push(node, node.pc)

    reach = {}
    reach[node.state] = node

    while (not (frontier.isEmpty())):
        node = (frontier.pop())
        if (node.state != problem.getStartState()):
            #print(node.dir)
            node.track.append(node.dir)

        if (problem.isGoalState(node.state)):
            return node.track
        
        for child in (problem.getSuccessors(node.state)):
            cn = Node(child)
            #print(cn.toString())
            if(cn.state not in reach) or (cn.pc < reach[cn.state].pc):
                cn.track = node.track + cn.track 
                #print(cn.track)
                cn.cost = node.cost + cn.pc
                reach[cn.state] = cn
                frontier.push(cn, cn.cost)
        #print()
    
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0
    
def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    node = Node(problem.getStartState())
    frontier = util.PriorityQueue() #by path cost
    frontier.push(node, node.pc)

    reach = {}
    print("nodeState", end = " ")
    print(node.state)
    reach[node.state[0]] = node

    while (not (frontier.isEmpty())):
        node = (frontier.pop())
        if (node.state != problem.getStartState()):
            #print(node.dir)
            node.track.append(node.dir)

        if (problem.isGoalState(node.state)):
            return node.track
        
        for child in (problem.getSuccessors(node.state)):
            cn = Node(child)
            #print(cn.toString())
            if(cn.state not in reach) or (cn.pc < reach[cn.state].pc):
                cn.track = node.track + cn.track 
                #print(cn.track)
                priorCost = node.cost + cn.pc + heuristic(cn.state, problem)
                cn.cost = node.cost + cn.pc
                reach[cn.state] = cn
                frontier.push(cn, priorCost)
    util.raiseNotDefined()


#cn.cost = heuristic(cn.state, problem) + cn.pc, + node.cost



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
