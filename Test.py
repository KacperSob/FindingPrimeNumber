n = 2
ktora = 1
while (True):
	flag = 0
	i = 2
	while i <= (n/2):
	    if (n%i) == 0:
	        flag = 1
	        break
	    i += 1
	if n == 1:
		print("error")
	elif flag == 0:
	    print(n, "to ", ktora, " liczba pierwsza")
	    ktora += 1
	n += 1
