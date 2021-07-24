# input: a column of numbers
# output: a histogram representing the distribution of the numbers
# bucket ranges for the histogram created according the data read
# data to be divided into n buckets of equal size

BEGIN { n = 10 }

NR == 1 { min = max = $1 }

{	input[NR] = $1
	if ($1 > max)
		max = $1
	if ($1 < min)
		min = $1
}

END {
	size = (max - min) / n
	for (i = 1; i <= NR; i++)
		x[int(input[i]/size)]++
	for (i = min; i < max; i += size) {
		y = x[int(i/size)]
		printf("%g - %g: %d %s\n", i, i + size, y, draw(y, "|"))
	}
	y = x[int(max/size)]
	printf("%g: %d %s\n", i, y, draw(y, "|"))
}

function draw(count, symbol) {
	str = ""
	for (j = 1; j <= count; j++)
		str = str symbol
	return str
}
