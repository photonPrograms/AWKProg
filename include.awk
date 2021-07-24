# Macro for expanding all the @include files and generate combined file
# Usage : awk -f include.awk <programfile.awk>
# Outputs : i<programfile.awk>

function include( progfile )
{

    while ( ( getline < progfile ) > 0 ) {

	if ( $1 == "@include" ) include( $2 )
	else print > ("itemp.awk")

	}

    close( progfile )

    if (ERRNO) print "error: " ERRNO > "/dev/stderr"

    return 1

} 



BEGIN {
    include( ARGV[1] )
    system("mv itemp.awk i" ARGV[1] )
}