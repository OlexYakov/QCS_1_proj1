# Report

2015231448 Oleksandr Yakovlyev

2017256029 Gustavo Morgado

2017254040 João Ramos

## Question 1

Peterson's solution (for two processes) achieves _mutual exclusion_ in a critical section. We verified this property in two ways:
- using a ghost variable and one assert
- using ltl's

## Question 2

In order model the processes stopping, possibly for an unlimited period, we implemented an if statement with two possible branches. The first branch has a skip statement, allowing for the process to continue as normal and request access to the critical region. The second statement stop the process using the logical statement (false). This means that each loop, because of Promela's non-deterministic nature, the process will have a 50-50 chance of either continuing to work as normal or stopping until a timeout.


## Question 3

```

bool turn , flag [2];
byte c;
byte check[2];

ltl deadlock_freedom { []( (check[0]==0) ->  <>(check[0]==1))  && [] ( (check[1]==0) ->  <>(check[1]==1)) }

active [2] proctype P ()
{
non_cs :
	check[_pid]++;
	if
	:: skip;
	:: true -> end: (false);
	fi
	check[_pid]--;
	
	
	flag [ _pid ] = 1; 					/* wants to enter critical section */
	turn = 1 - _pid ;					/* politely give turn to the other one */
	(! flag [1 - _pid ] || turn == _pid );	/* block until the other doesn ’ t want */
												/* OR it is this one ’ s turn */
cs :
	c++;
	check[_pid]++;
	assert(c == 1);
	skip ;
	check[_pid]--;
	c--;									/* critical section */
exit :
	flag [ _pid ] = 0;						/* leaves the critical section */
	goto non_cs
}
```


In order to test the lack of deadlocks in our model, we used following ltl formula:

```
[]( (check[0]==0) -> <>(check[0]==1)) && [] ( (check[1]==0) -> <>(check[1]==1))
```

Each process has a check variable that is incremented after entering the critical region and decremented before leaving it. The ltl formula dictates that every time a check variable is 0 it will eventually become 1. This is only true if the processes can enter the critical section, and, therefore, if there are no deadlocks in the model.
The values of the check variable are also incremented and decremented around the code made in question 2 to ensure that the ltl wouldn't create an error if the processes stoped without wanting to enter the critical region since that is not a deadlock. Since each process has it's own check variable we can do this without having to worry about interferences from the other process. It serves the same purpose as a end label in the if statement. 

## Question 4
The philosophers are modeled by processes, and the forks are modeled by a global integer array _forks_, of size N, such that a philosopher with PID _p_ holding fork _i_ is represented as _forks_[ _i_ ] = _p_.
To be fair and let all philosophers sit at the table at the same time, we start all the processes atomically in the _init_ function.

```
# define N 5
# define LEFT _pid - 1
# define RIGHT _pid % N

int forks[N];

proctype Phil () {
...
}

init {
	byte i;
	atomic {
		for (i : 0 .. N-1){
			run Phil();
		}
	}
}
```

The model has two possible states for each philosopher: thinking and eating. To go from thinking to eating the philosopher must pick up two forks, one at each side.

Our first attempt lets the philosopher pick a fork on his left or right, at random, but he can only eat when both forks are in his possession. We implemented this with a do loop with three (possibly blocking) alternatives, corresponding the following options:

1. if free, pick the left fork
2. if free, pick the right fork
3. if has both forks, proceed to eat

The corresponding code:

```
proctype Phil(){
    do
	::
		// THINK
		printf("philosopher %d thinks ...\n" , _pid );
		
		short nforks = 0;
		/* pick up left and right forks if available */
		do
		::	forks[LEFT] == 0 -> 
				forks[LEFT] = _pid;
				nforks++;
		::	forks[RIGHT] == 0 ->
				forks[RIGHT] = _pid;
				nforks++;
		::	nforks == 2 -> break;
		od
		
		// EAT		
		printf("philosopher %d eats ...\n" , _pid );
		
		/* put the two forks down */
		forks[LEFT] = 0;
		forks[RIGHT] = 0;
	
	od
}
```

The idea is that the philosophers only pick up a fork if no one is holding it - in practice we have a guard (ex: `forks[LEFT] == 0`) that blocks the action of assigning the fork the current philosopher (ex: `forks[LEFT] = _pid`). The loop can only break if the number of forks held is two.
As expected, the output _seems_ to be correct, but as the following questions will demonstrate it is not. This is because the evaluation of the guard and the execution of the guarded statements is not an atomic operation, meaning that two or more philosophers could evaluate the guard to `true` before any of them had time to claim ownership.

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
              P5   |[0] [1] [2] [3] [4]| 
---------------------------------------|                   
5 Phil:       0    | 5   2   3   4   0 |         
5 Phil:       1    | 5   2   3   4   0 |         
5 Phil:       1    | 5   2   3   4   0 |    <-- Process 5 acquired left fork 4
4 Phil:       1    | 5   2   3   4   5 |    <-- Process 4 acquired right fork 4 even if held by 5
5 Phil:       1    | 5   2   3   4   4 |    <-- Process 5 still thinks he has two forks, increments n. forks to 2
4 Phil:       2    | 5   2   3   4   4 |         
5 Phil:       2    | 5   2   3   4   4 |         
spin: philosophers.pml:31, Error: assertion violated
spin: text of failed assertion: assert(((forks[(_pid-1)]==_pid)&&(forks[(_pid%5)]==_pid)))
                                        ...
```
_(the output is slightly modified to fit the screen)_

As we can see, no synchronization means that even tough there is a guard (`forks[LEFT] == 0`) we do not have mutual exclusion. 
Both process 4 and 5 checked the guard and saw that fork 4 was free, and both went into the guarded statements, as predicted.
Philosopher 5 claimed ownership and that was overridden right away by Philosopher 4.

In conclusion, both properties were violated. Philosopher 4 took a fork that was already in use (property 1) and Philosopher 5 was ready to eat even though he didn't have both forks (property 2).

## Question 7
In this iteration of the program we implemented mutual exclusion for each fork resource.
Initially we thought that this was a problem of synchronization between N processes, but even though each fork is a shared resource, it is only ever accessed by two philosophers. This means that what we have is many instances of synchronization for N=2 processes, which can be solved with the provided Peterson's algorithm.

We implemented two functions, `lock(n)` and `unlock(n)`, that as the names suggest, create a critical region accessible only by the processes that currently holds the lock. This way each philosopher has to acquire the lock _n_ before picking up the fork _n_.

Auxiliary functions:
```
# define FK(a) ((_pid - (a)) % N)

bool flag[N*2];
# define MAT(i,j) flag[(i)*2+(j)]

bool turn[N];

inline lock(n){
	MAT(n,FK(n)) = 1;
	turn[n] = 1- FK(n);
	(!MAT(n,1- FK(n)) || turn[n] == FK(n));
	
}

inline unlock(n){
	MAT(n,FK(n)) = 0;
}
```

Inner loop changes: now, each philosopher acquires the lock before writing to the `forks` array
```
...
proctype Phil () {
    ...
        // Inner loop changes
		do
		::	forks[LEFT] != _pid -> 
				lock(LEFT);
				forks[LEFT] = _pid;
				nforks++;
				
		::	forks[RIGHT] != _pid ->
				lock(RIGHT);
				forks[RIGHT] = _pid;
				nforks++;
				
		::	nforks == 2 -> break;
		od
	...

    // Release both forks in the end   
    unlock(LEFT);
    unlock(RIGHT);
	
}

```

With this solution the random simulation output was one of the two: 
* invalid-end statement : there was a deadlock
* depth-limit reached: we tried with MAX_STEPS 2500 and MAX_DEPTH 200_000 and there were no deadlocks (so far) and no assertion violations.

The verify option ended on an invalid end state, but when run with the -E flag (disables invalid end state checks) we always had the max depth too small error, but no assertions error.

This means that we achieved the _safety property_ of _mutual exclusion_ in respect to the forks.
...

## Question 8

In order to test for deadlock freedom, we simply used Spin's verify with invalid end states turned on. Using this configuration if the processes are blocked and haven't reached the closing brackets (end state), Spin will produce a invalid end state error. Since in our model there are no acceptable states for a process to block on, we don't need end labels.

We tested it against our current model and got a invalid end state error. After some consideration, we realized this happened because while accessing each fork was mutually exclusive, the order in which the forks where accessed was random and there was nothing stopping a process of getting permanently stuck waiting for access to a fork if another process didn't release it.
It was therefore possible to reach a deadlock where processes were all blocking each other: for example, a situation where everyone is holding the left fork.

## Question 9
To avoid deadlocks, we decided to implement an order on the available forks and make it so that all philosophers pick the fork with the lowest number first, corresponding to their position.

Here is a diagram for better visualization:

![Diagram of Philosophers and forks](diagram.png)

And here is the corresponding code:
```
byte first;
byte second;
if 
::	(LEFT < RIGHT) -> 
        first = LEFT;
        second = RIGHT;
::	else ->
        first = RIGHT;
        second = LEFT;
fi
```
By making this, all the philosophers will pick up the left fork, with the exception of the fifth philosopher, who will try to reach the right fork. Due to this, there will be a competition between philosopher 1 and 5, where the first  one that picks the fork will be able to eat, which will then uphold the property that some philosophers that want to eat will eventually do so.

This will also uphold the property of them being silent, since there is no need for communication between them. For the cases where a philosopher can be stuck thinking, we implemented the method used in question 2. However, because it's not a full deadlock, we had to implement the end label, to show that if the philosopher ends up on that line it ends the process, as intended, so that Spin doesn't attribute an invalid end state error.

```
// THINK
printf("philosopher %d thinks ...\n" , _pid );

if
:: skip;
:: skip;
:: true -> end: (false);
fi

/* pick up left and right forks if available */
short nforks = 0;
```

## Question 10

Weak fairness does not affect the correctness properties of our model. The first property that states that "there may never be any single fork being held by more than one philosopher simultaneously" is assured by our locks, since, because of them, there can only be one process having access to a fork no matter how it is scheduled. The second property, "every philosopher only eats when holding both the left and the right fork",  is true because to eat a process must acquire access to both its left and right forks, passing both locks.
Mutual exclusion is also ensured by the locks, regardless of how the processes are scheduled. Lastly, deadlock freedom is ensured because the rules stated in question 9 in conjunction with the mutual exclusion ensure that at least one process will always be executing.

But there is another question concerning fairness: is the algorithm fair in respect to the philosophers? Do all the philosophers get to eat ? In other words, is there a possibility that one philosopher (that wants to eat) never gets a chance?
Our solution does not guarantee this kind of fairness. If, for example, one of the philosophers was slow to take a fork and his peer was faster to think and pick the fork back up, he can never get the chance to eat.
This is known as starvation.
