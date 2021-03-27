#define rand	pan_rand
#define pthread_equal(a,b)	((a)==(b))
#if defined(HAS_CODE) && defined(VERBOSE)
	#ifdef BFS_PAR
		bfs_printf("Pr: %d Tr: %d\n", II, t->forw);
	#else
		cpu_printf("Pr: %d Tr: %d\n", II, t->forw);
	#endif
#endif
	switch (t->forw) {
	default: Uerror("bad forward move");
	case 0:	/* if without executable clauses */
		continue;
	case 1: /* generic 'goto' or 'skip' */
		IfNotBlocked
		_m = 3; goto P999;
	case 2: /* generic 'else' */
		IfNotBlocked
		if (trpt->o_pm&1) continue;
		_m = 3; goto P999;

		 /* PROC P */
	case 3: // STATE 1 - exe_2.pml:7 - [stop = 0] (0:0:1 - 1)
		IfNotBlocked
		reached[0][1] = 1;
		(trpt+1)->bup.oval = ((P0 *)_this)->stop;
		((P0 *)_this)->stop = 0;
#ifdef VAR_RANGES
		logval("P:stop", ((P0 *)_this)->stop);
#endif
		;
		_m = 3; goto P999; /* 0 */
	case 4: // STATE 2 - exe_2.pml:7 - [stop = 1] (0:0:1 - 1)
		IfNotBlocked
		reached[0][2] = 1;
		(trpt+1)->bup.oval = ((P0 *)_this)->stop;
		((P0 *)_this)->stop = 1;
#ifdef VAR_RANGES
		logval("P:stop", ((P0 *)_this)->stop);
#endif
		;
		_m = 3; goto P999; /* 0 */
	case 5: // STATE 3 - exe_2.pml:7 - [stop = 2] (0:0:1 - 1)
		IfNotBlocked
		reached[0][3] = 1;
		(trpt+1)->bup.oval = ((P0 *)_this)->stop;
		((P0 *)_this)->stop = 2;
#ifdef VAR_RANGES
		logval("P:stop", ((P0 *)_this)->stop);
#endif
		;
		_m = 3; goto P999; /* 0 */
	case 6: // STATE 4 - exe_2.pml:7 - [stop = 3] (0:0:1 - 1)
		IfNotBlocked
		reached[0][4] = 1;
		(trpt+1)->bup.oval = ((P0 *)_this)->stop;
		((P0 *)_this)->stop = 3;
#ifdef VAR_RANGES
		logval("P:stop", ((P0 *)_this)->stop);
#endif
		;
		_m = 3; goto P999; /* 0 */
	case 7: // STATE 5 - exe_2.pml:7 - [stop = 4] (0:0:1 - 1)
		IfNotBlocked
		reached[0][5] = 1;
		(trpt+1)->bup.oval = ((P0 *)_this)->stop;
		((P0 *)_this)->stop = 4;
#ifdef VAR_RANGES
		logval("P:stop", ((P0 *)_this)->stop);
#endif
		;
		_m = 3; goto P999; /* 0 */
	case 8: // STATE 6 - exe_2.pml:7 - [stop = 5] (0:0:1 - 1)
		IfNotBlocked
		reached[0][6] = 1;
		(trpt+1)->bup.oval = ((P0 *)_this)->stop;
		((P0 *)_this)->stop = 5;
#ifdef VAR_RANGES
		logval("P:stop", ((P0 *)_this)->stop);
#endif
		;
		_m = 3; goto P999; /* 0 */
	case 9: // STATE 7 - exe_2.pml:7 - [stop = 6] (0:0:1 - 1)
		IfNotBlocked
		reached[0][7] = 1;
		(trpt+1)->bup.oval = ((P0 *)_this)->stop;
		((P0 *)_this)->stop = 6;
#ifdef VAR_RANGES
		logval("P:stop", ((P0 *)_this)->stop);
#endif
		;
		_m = 3; goto P999; /* 0 */
	case 10: // STATE 8 - exe_2.pml:7 - [stop = 7] (0:0:1 - 1)
		IfNotBlocked
		reached[0][8] = 1;
		(trpt+1)->bup.oval = ((P0 *)_this)->stop;
		((P0 *)_this)->stop = 7;
#ifdef VAR_RANGES
		logval("P:stop", ((P0 *)_this)->stop);
#endif
		;
		_m = 3; goto P999; /* 0 */
	case 11: // STATE 9 - exe_2.pml:7 - [stop = 8] (0:0:1 - 1)
		IfNotBlocked
		reached[0][9] = 1;
		(trpt+1)->bup.oval = ((P0 *)_this)->stop;
		((P0 *)_this)->stop = 8;
#ifdef VAR_RANGES
		logval("P:stop", ((P0 *)_this)->stop);
#endif
		;
		_m = 3; goto P999; /* 0 */
	case 12: // STATE 10 - exe_2.pml:7 - [stop = 9] (0:0:1 - 1)
		IfNotBlocked
		reached[0][10] = 1;
		(trpt+1)->bup.oval = ((P0 *)_this)->stop;
		((P0 *)_this)->stop = 9;
#ifdef VAR_RANGES
		logval("P:stop", ((P0 *)_this)->stop);
#endif
		;
		_m = 3; goto P999; /* 0 */
	case 13: // STATE 11 - exe_2.pml:7 - [stop = 10] (0:0:1 - 1)
		IfNotBlocked
		reached[0][11] = 1;
		(trpt+1)->bup.oval = ((P0 *)_this)->stop;
		((P0 *)_this)->stop = 10;
#ifdef VAR_RANGES
		logval("P:stop", ((P0 *)_this)->stop);
#endif
		;
		_m = 3; goto P999; /* 0 */
	case 14: // STATE 14 - exe_2.pml:8 - [(stop)] (0:0:1 - 12)
		IfNotBlocked
		reached[0][14] = 1;
		if (!(((P0 *)_this)->stop))
			continue;
		if (TstOnly) return 1; /* TT */
		/* dead 1: stop */  (trpt+1)->bup.oval = ((P0 *)_this)->stop;
#ifdef HAS_CODE
		if (!readtrail)
#endif
			((P0 *)_this)->stop = 0;
		_m = 3; goto P999; /* 0 */
	case 15: // STATE 15 - exe_2.pml:10 - [flag[_pid] = 1] (0:0:1 - 1)
		IfNotBlocked
		reached[0][15] = 1;
		(trpt+1)->bup.oval = ((int)now.flag[ Index(((int)((P0 *)_this)->_pid), 2) ]);
		now.flag[ Index(((P0 *)_this)->_pid, 2) ] = 1;
#ifdef VAR_RANGES
		logval("flag[_pid]", ((int)now.flag[ Index(((int)((P0 *)_this)->_pid), 2) ]));
#endif
		;
		_m = 3; goto P999; /* 0 */
	case 16: // STATE 16 - exe_2.pml:11 - [turn = (1-_pid)] (0:0:1 - 1)
		IfNotBlocked
		reached[0][16] = 1;
		(trpt+1)->bup.oval = ((int)now.turn);
		now.turn = (1-((int)((P0 *)_this)->_pid));
#ifdef VAR_RANGES
		logval("turn", ((int)now.turn));
#endif
		;
		_m = 3; goto P999; /* 0 */
	case 17: // STATE 17 - exe_2.pml:12 - [((!(flag[(1-_pid)])||(turn==_pid)))] (0:0:0 - 1)
		IfNotBlocked
		reached[0][17] = 1;
		if (!(( !(((int)now.flag[ Index((1-((int)((P0 *)_this)->_pid)), 2) ]))||(((int)now.turn)==((int)((P0 *)_this)->_pid)))))
			continue;
		_m = 3; goto P999; /* 0 */
	case 18: // STATE 19 - exe_2.pml:17 - [flag[_pid] = 0] (0:0:1 - 1)
		IfNotBlocked
		reached[0][19] = 1;
		(trpt+1)->bup.oval = ((int)now.flag[ Index(((int)((P0 *)_this)->_pid), 2) ]);
		now.flag[ Index(((P0 *)_this)->_pid, 2) ] = 0;
#ifdef VAR_RANGES
		logval("flag[_pid]", ((int)now.flag[ Index(((int)((P0 *)_this)->_pid), 2) ]));
#endif
		;
		_m = 3; goto P999; /* 0 */
	case  _T5:	/* np_ */
		if (!((!(trpt->o_pm&4) && !(trpt->tau&128))))
			continue;
		/* else fall through */
	case  _T2:	/* true */
		_m = 3; goto P999;
#undef rand
	}

