# check jwhois for domain & print DNS

{

    while (("jwhois "$0 | getline var) > 0 ) {

	if (var ~ /Name Server:(\w|\.|-)+/ && c == 0) {
	 gsub( /Name Server:/ , "" , var ) 
	 print $0 "\t" var
	    c = 1
	}

	else if ( var ~ /Name Server:(\w|\.|-)+/ && c == 1) c = 0
	

	if ( var ~ /Servers/ ) {
	    n = 1
	    
	}
	
	else if ( n == 1 ) {
	    print $0 "\t" var
	    n = 0
	}


    }

    close("jwhois "$0)

}