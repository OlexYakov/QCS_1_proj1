# define N 5
# define LEFT _pid - 1
# define RIGHT _pid % N
# define FK(a) ((_pid - (a)) % N)

bool have_eaten[N];
int eaten;
ltl starvation { <>(eaten >= 1)}

int forks[N];

bool flag[N*2];
# define MAT(i,j) flag[(i)*2+(j)]

bool turn[N];



inline lock(n){
	//printf("LOCK pid (%d) f %d\n",_pid,n);
	MAT(n,FK(n)) = 1;
	//printf("MAT %d\n",MAT(n,FK(n)));
	turn[n] = 1- FK(n);
	//printf("turn %d\n",turn[n]);
	//printf("c1 %d\tc2 %d\n",!MAT(n,1- FK(n)) ,turn[n] == FK(n));
	(!MAT(n,1- FK(n)) || turn[n] == FK(n));
	
}

inline unlock(n){
	MAT(n,FK(n)) = 0;
}

proctype Phil () {
	
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

	do
	::
		// THINK
		printf("philosopher %d thinks ...\n" , _pid );
		


		/* pick up left and right forks if available */
		short nforks = 0;
		
		lock(first)
		forks[first] = _pid;
		nforks++;
	
		lock(second)
		forks[second] = _pid;
		nforks++;
		
		// EAT		
		assert(forks[LEFT] == _pid && forks[RIGHT] == _pid);
		printf("philosopher %d eats ...\n" , _pid );
		
		if
		::	!have_eaten[_pid-1] -> 
				have_eaten[_pid-1] = true;
				eaten++;
		::	else -> break;
		fi

		/* put the two forks down */
		
		forks[first] = 0;
		unlock(first);
		forks[second] = 0;
		unlock(second);

		if
		:: skip;
		:: skip;
		:: true -> end: (false);
		fi
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