function splitz(s,m,u,regexp,    i,j,n ) {
    #exports arrays u and m i.e. unmatched string & matched string
    #returns no. of matches, if none then returns 0

    delete u
    delete m
    while ( match( s , regexp ) ) {

	u[++i] = substr( s, 1, RSTART-1 )
	m[++j] = substr( s, RSTART, RLENGTH )
	s = substr( s, RSTART+RLENGTH )
	++n
    }

    if (!match( s , regexp ) ) {
	u[++i] = s
	m[++j] = ""
    }

    return n+0

}