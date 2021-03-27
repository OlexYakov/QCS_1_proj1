bool turn , flag [2];
byte c;
byte mutex = 0;
ltl deadlock_freedom { []( (mutex==0) ->  <>(mutex==1)) }
active [2] proctype P ()
{
non_cs :
	
	if
	:: skip;
	:: true -> end: (false);
	fi

	flag [ _pid ] = 1; 						/* wants to enter critical section */
	turn = 1 - _pid ;						/* politely give turn to the other one */
	(! flag [1 - _pid ] || turn == _pid );	/* block until the other doesn ’ t want */
												/* OR it is this one ’ s turn */
cs :
	c++;
	mutex++;
	assert(c == 1);
	skip ;
	mutex--;
	c--;									/* critical section */
exit :
	flag [ _pid ] = 0;						/* leaves the critical section */
	goto non_cs
}
