# 4511 Project
# Dead by Daylight Pacman Project

## Purpose

Solving simplified Dead by Daylight that implemented as Pacman in order to find best possible ways to win against ghost (killer in the original game). The hope is for this to be able to help planing strategies for players. 

## Implementation and Simplification

## State

For an m-by-n map, k food, s time, 4 pacmans, and 1 ghost.

Each square on the map can either have food or not. If the square have a food, then it possible to have
1. Nothing
2. $s$ variations of food status
3. Four possible pacmans
4. One ghost

For square without the food, it can hold the following states:
1. Nothing
2. Four possibles pacmans
3. A ghost

The state space overall become
$$
\left(
\binom{n \times m}{k}
\right) ^ {s+6} 
\times 
\left( 
\binom{n \times m}{(n \times m) - k}
\right) ^ {6} $$


## Actions
