# Report

2015231448 Oleksandr Yakovlyev

## Question 1

Petersons solution (for two processes) achieves _mutual exclusion_ in a critical section. We verified this property in two ways:
- using a ghost variable and one assert
- using ltl's

## Question 2

## Question 3

## Question 4

The philosophers are modeled by processes, and the forks are modeled by a global integer array _forks_, of size N, such that a philosopher with PID _p_ holding fork _i_ is represended as _forks_[ _i_ ] = _p_.
To be fair and let all philosophers sit at the table at the same time, we start all the processes atomicaly in the _init_ function.

So far the model has two possible states for each philosopher: thinking and eating. To go from thinking to eating the philosopher must pick up two forks, one at each side.



The loop has three possibly blocking alternatives, corresponding the following options:
1. Pick up the left fork
2. Pick up the right fork
3. Break the loop and proceed to eat


## Question 5

## Question 6

## Question 7

## Question 8

## Question 9

## Question 10