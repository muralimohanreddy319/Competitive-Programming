def sorted_height(list):
	
	for i in range(len(list)-1):
		high = list[i][0]
		index=i
		for j in range(i+1,len(list)):
			if(list[j][0]>high):
				index=j
				high = list[j][0]
		list[i],list[index]=list[index],list[i]
	return list

print sorted_height([[12,0],[6,3],[3,4],[9,2], [11,1],[1,5]])
print sorted_height([ [2,4], [5,1], [3,3], [1,5], [4,2], [6,0]])
