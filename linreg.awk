# input: a text file with data for the regression calculation
# output: the regression calculations

BEGIN {
	OFS = FS = "\t"
	totx = 0
	toty = 0
}

{	x[NR] = $1
	y[NR] = $2
	totx += $1
	toty += $2
}

END {
	xavg = totx / NR
	yavg = toty / NR
	tot1 = 0
	tot2 = 0
	for (i = 1; i <= NR; i++) {
		xdiff[i] = x[i] - xavg
		ydiff[i] = y[i] -yavg
		xydiff[i] = xdiff[i] * ydiff[i]
		xsqdiff[i] = xdiff[i] * xdiff[i]
		tot1 += xydiff[i]
		tot2 += xsqdiff[i]
	}
	m = tot1 / tot2
	c = yavg - m * xavg
	for (i = 1; i <= NR; i++)
		printf("%g\t%g\t%.4f\t%.4f\t%.8f\t%.8f\n", x[i], y[i], xdiff[i], ydiff[i], xydiff[i], xsqdiff[i])
		#print x[i] "\t" y[i] "\t" xdiff[i] "\t" ydiff[i] "\t" xydiff[i] "\t" xsqdiff[i]
	printf("total x = %f\n", totx)
	printf("total y = %f\n", toty)
	printf("x_avg = %.4f\n", xavg)
	printf("y_avg = %.4f\n", yavg)
	printf("xytotal = %.8f\n", tot1)
	printf("xsqtotal = %.8f\n", tot2)
	printf("slope = %.8f\n", m)
	printf("y-intercept = %.8f\n", c)
}
