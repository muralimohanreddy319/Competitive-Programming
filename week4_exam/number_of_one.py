def binary(num):
	l=[]
	print num
	for i in range(num+1):
		# print i
		l1=list(bin(i)[2:])
		# print l1
		count=0
		for i in l1:
			if(i=='1'):
				count+=1
		l.append(count)
	return l

print binary(15)
print binary(16)
print binary(1)
print binary(25)
print binary(5)
print binary(6)
