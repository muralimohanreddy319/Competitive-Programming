def water_trap(list1):
	l=[False]*len(list1)
	# print list1
	count =0
	for i in range(len(list1)-1):
		if(l[i]==False):
			temp1=i
			# print i
			# print temp1s
			second_largest=0
			for j in range(i+1,len(list1)):
				# if(list1[j]>second_largest):
				# 	second_largest=list1[j]
				# if(j==len(list1)-1):
				# 	l,x=trap(temp1,(j),l,list1[temp1:(j+1)])
				# 	count+=x
				# 	break
				if(l[j]==False):
					# print j
					if(list1[j]>=list1[temp1]):
						l,x=trap(temp1,(j),l,list1[temp1:(j+1)])
						count+=x
						break
	return count

def trap(temp1,x,l,list1):
	lar=max(list1)
	sl=0
	print list1
	for i in range(len(list1)):
		if(list1[i]>sl and list1[i]<lar):
			sl=list1[i]

	for i in range(temp1,x):
		l[i]=True
		
	count=0
	print sl
	for i in range(len(list1)):
		k=sl-list1[i]
		if(k>0):
			print k
			count+=k
	return l,count



print water_trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
# print water_trap([0, 1, 0, 2, 1, 0, 1])
# print water_trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
# print water_trap([0, 1, 0, 2, 1, 0, 5, 1, 0, 2])

# print water_trap([0, 1, 0, 5, 1, 0, 2])
# print water_trap([0, 5, 1, 3, 4, 0, 1])


