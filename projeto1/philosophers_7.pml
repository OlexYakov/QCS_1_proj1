# define N 5
# define LEFT _pid - 1
# define RIGHT _pid % N
# define FK(a) ((_pid - (a)) % N)

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


	do
	::
		// THINK
		printf("philosopher %d thinks ...\n" , _pid );
		
		/* pick up left and right forks if available */
		short nforks = 0;

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
		
		// EAT		
		assert(forks[LEFT] == _pid && forks[RIGHT] == _pid);
		printf("philosopher %d eats ...\n" , _pid );
		
		/* put the two forks down */
		
		forks[LEFT] = 0;
		unlock(LEFT);
		forks[RIGHT] = 0;
		unlock(RIGHT);
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