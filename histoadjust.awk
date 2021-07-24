# input: a column of numbers between 0 and 100
# output: histogram of decile buckets
# also does not allow the bars of the graph to
# overflow in any line
# using maximum character length n

{ x[int($1/10)]++ }

END {
	n = MAXSTARS = 25
	for (i = 0; i <= 10; i++)
		if (x[i] > n)
			n = x[i]
	for (i = 0; i <= 10; i++)
		y[i] = x[i] / n * MAXSTARS
	for (i = 0; i < 10; i++)
		printf("%2d - %2d: %3d %s\n", i*10, i*10+9, x[i], drawgen(y[i], "*"))
	printf("100: %7d %s\n", x[10], drawgen(y[10], "*"))
}

function drawgen(count, symbol) {
	str = ""
	for (j = 1; j <= count; j++)
		str = str symbol
	return str
}
