#To do operation (e.g. toupper here) on all matched regexps
#use - e.g. print splitz_op($0,".[a-z].")

function splitz_op(s,regexp,     mod_str,i,j,k)

{
    mod_str = ""
    
    splitz(s,m,u,regexp) #called splitz function for m,u arrays creation
    
    for(i=1; i<=length(m); i++)
	m[i] = toupper(m[i]) #change here for some other operation

    j = 1
    k = 1
    while(j <= length(u) || k <= length(m)) {
	
	mod_str = mod_str u[j] m[k]
	j++
	k++
	
    }

    delete u
    delete m
    return mod_str

}



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