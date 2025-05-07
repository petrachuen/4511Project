# Dead by Daylight Pacman Project

## Motivation for this project

Dead by Daylight is an online multiplayer survival horror game. Typically, there are four survivors and one killer which survivors have to fix all generator to escape and win (even if only one survivor survived) while the killer have to kill all of the survivor to win. For more detailed information [Dead by Daylight Official Website](https://deadbydaylight.com/). 

This project therefore aimed to find the optimal solution for survivor to be able to win the game. However, this is the simplified version of the game using Pacman as a representation. 

The game representation are as follows
- Pacman represented Killer
- Four ghosts represented survivors
- Food represented generator



























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
$$\left(\binom{n \times m}{k}\right) ^ {s+6} \times \left( \binom{n \times m}{(n \times m) - k}\right) ^ {6} $$


## Actions

### Pacman Actions
1. Moves: Right, Left, Up, Down, Stop
2. Eating: Consume one food's timesteps for a move

### Ghost Actions
1. Moves: Right, Left, Up, Down, Stop
2. Eating: Ghost can eat pacman if they are on the same squre
3. Special move
   - ghost can choose to relocate, in one step, to be next to a Pacman.
   - If the ghost chooses to use this, it can not use again until at least 2 timestep of Pacman’s food-eating time

### Food
- Each food have a 'timestep' (representing generator in the original game)
- If Pacman leaves the food before it is completely eaten
   - The food time adds half of what’s left.
   - Example: Food needs to be eaten in 10 time steps
        - If Pacman leaves when 6 time steps are left to complete, then the food now needs 9 time steps to be completed. 
