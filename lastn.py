def read_lines(fname,n,mode='r+'):
	with open(fname) as f:
		for i in range(n):
			print(f.readline())

read_lines('sarika.txt',4)