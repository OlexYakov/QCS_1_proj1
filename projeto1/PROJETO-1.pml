bool turn , flag [2];
byte c = 0;
active  [2]  proctype P(){
	non_cs:
		flag[_pid] = 1;    /* wants to  enter  critical  section      */
		turn = 1 - _pid;    /*  politely  give  turn to the  other  one */
		(!flag[1 - _pid] || turn == _pid);  /* block  until  the  other  doesn ’t want   *
	/* OR it is this one ’s turn               */
		c++;
	cs:
		skip;                                   /*  critical  section                        */
		assert(c == 1);
	exit:
		c--;
		flag[_pid] = 0;                        /*  leaves  the  critical  section           */
	goto  non_cs
}