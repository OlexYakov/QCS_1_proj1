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