# Gets the file as a single string
# Usage: getfile(inputfile[, newarr[, rsnew]]) --> returns file as a string
# Warning: if rsnew is used, then newarr must also be provided e.g. patcharr
# if rsnew is not provided, then the existing RS is used

function getfile( inputfile, newarr, rsnew,      rsold, n, wholefilestr ) 

{

    rsold = RS

    if (rsnew)
	RS = rsnew

    delete getfilearr  # prepare & later exports records array
    delete rtarr       # exports RT array (where rtarr[n] is usually "")
    delete newarr
    
    while ( (getline getfilearr[++n] < inputfile) > 0 ) {
	rtarr[n] = RT
	wholefilestr =  wholefilestr getfilearr[n] rtarr[n]
	newarr[n] = getfilearr[n]

    }

    close(inputfile)

    RS = rsold

    return wholefilestr

}