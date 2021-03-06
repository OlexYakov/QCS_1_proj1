# define N 5
# define LEFT _pid - 1
# define RIGHT _pid % N

int forks[N];

proctype Phil () {


	do
	::
		// THINK
		printf("philosopher %d thinks ...\n" , _pid );
		
		/* pick up left and right forks if available */
		short nforks = 0;
	
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
		//assert(forks[LEFT] == _pid);	// Question 4
		//assert(forks[RIGHT] == _pid);	// Question 4
		assert(forks[LEFT] == _pid && forks[RIGHT] == _pid);
		printf("philosopher %d eats ...\n" , _pid );
		
		/* put the two forks down */

		forks[LEFT] = 0;
		forks[RIGHT] = 0;
	
	od
}

init {
	byte i;
	atomic {
		for (i : 0 .. N-1){
			run Phil();
		}
	}
}