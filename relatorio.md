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

The model has two possible states for each philosopher: thinking and eating. To go from thinking to eating the philosopher must pick up two forks, one at each side.

Our first atempt lets the philosopher pick a fork on his left or right, at random, but he can only eat when both forks are in his possession. We implemented this with a do loop with three (possibly blocking) alternatives, corresponding the following options:

1. if free, pick the left fork
2. if free, pick the right forks
3. if has both forks, proceed to eat


## Question 5 and 6
Correctness properties:
* there may never be any single fork being held by more than one philosopher simultaneously
* every philosopher only eats when holding both the left and the right fork

The first property can be verified by asserting that, between the moment that the fork is explicitly picked up and consequently put down, it's always held by the same philosopher.

```
forks[LEFT] = _pid;             // pick up the fork
...
assert(forks[LEFT] == _pid);
...
forks[LEFT] = 0;                // put down
```

The same is applied to both left and right forks and, at this point, the second property is also verified:
```
assert(forks[LEFT] == _pid && forks[RIGHT] == _pid);
```

We ran the verification with the -E flag to disable invalid end states checks (because at this point deadlocks are a problem) and, as expected, the assertion failed.
After examining the detailed output from the guided run option the problem was evident:
```
Process  | n.forks |       forks        |                                         
              P5   | [0] [1] [2] [3] [4]| 
----------------------------------------|                   
5 Phil:       0    |  5   2   3   4   0 |         
5 Phil:       1    |  5   2   3   4   0 |         
5 Phil:       1    |  5   2   3   4   0 |         <-- Process 5 aquired left fork 4
4 Phil:       1    |  5   2   3   4   5 |         <-- Process 4 aquired right fork 4 even if held by 5
5 Phil:       1    |  5   2   3   4   4 |         <-- Process 5 still thinks he has two forks, increments n. forks to 2
4 Phil:       2    |  5   2   3   4   4 |         
5 Phil:       2    |  5   2   3   4   4 |         
spin: philosophers.pml:31, Error: assertion violated
spin: text of failed assertion: assert(((forks[(_pid-1)]==_pid)&&(forks[(_pid%5)]==_pid)))
                                        ...
```
(the output is slightly modified to fit the screen)

As we can see, no syncronization means that even tough there is a guard (forks[_pid] == 0) we do not have mutual exlusion. 
Both process 4 and 5 checked the guard and saw that fork 4 was free, and both went into the guarded statements.
Philosopher 5 claimed ownership and that was overiden right away by Philosopher 4.

In conlusion, both properties were violated. Philosopher 4 took used a fork that was already in use (property 1) and Philosopher 5 was ready to eat even though he didn't have both forks.
## Question 7

## Question 8

## Question 9

## Question 10