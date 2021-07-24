# Takes uncoded string str & returns encoded str - with reserved chars (i.e.
# except alnum - ~ . % ) encoded as %hex, \n -> CR LF , " " -> +

function encodeurl ( str  ,         i , hexnum , symbol , hexchar , j , jesc)

{

    for ( i=1  ; i<256  ; i++  ) {
	hexnum[i] = sprintf( "%x" , i  )
	symbol[i] = sprintf( "%c", strtonum("0x"hexnum[i]) )
	hexchar[(symbol[i])] = "%" hexnum[i]
    }

    
    gsub( /\n/ , "%0D%0A" , str  )

    for ( j in hexchar ) {
	
	if (j ~ /[[:graph:]]/ && j != "" && j !~ /\w|%|\.|-|~/) {
	    
	    if (j !~ /[<>`']/) {
		jesc = "\\" j
		str = gensub( jesc , hexchar[j] , "g" , str )
	    } else {
		str = gensub( j , hexchar[j] , "g" , str )
	    }

	}

    }

    gsub( / / , "+" , str )
    
    return str

}