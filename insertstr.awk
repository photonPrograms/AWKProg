# Returns the string containing inserted substring at "where" e.g. 0.5, 0.75 

function insertstr( mainstr, insstr, where,      i )
{

    for ( i = int(length(mainstr) * where) ;
	  substr(mainstr,i,1) != " " && i < length(mainstr) ;
	  i++ )
	continue
    
    
    if (substr(mainstr, i-1, 1) == ".")
	mainstr = substr(mainstr,1,i-2) " " insstr " " substr(mainstr,i+1)
    else
	mainstr = substr(mainstr,1,i-1) " " insstr " " substr(mainstr,i+1)
   

    return mainstr

}