from process import Process

list_of_process = []

def run(n, list):
	wt = 0
	ta = 0
	for i in range(0, n ):
		list[i].wt = int(wt)
		list[i].ta=  int(list[i].te) + ta
		wt = int(list[i].te) + int(wt)
		ta = ta + int(list[i].te)

	wt = wt - int(list[n-1].te)
	# print('---------------------------')
		
	print( "Processes Burst time " +
			" Waiting time " +
			" Turn around time")

	for i in range(0, n ):
		print(" " + str(i + 1) + "\t\t" +
		str(list[i].te) + "\t " +
		str(list[i].wt) + "\t\t " +
		str(list[i].ta) + "\t\t " )

	print( "Average waiting time = "+ str(wt / n))
	print("Average turn around time = "+  str(ta / n))

	# print(wt)
	# print(ta)