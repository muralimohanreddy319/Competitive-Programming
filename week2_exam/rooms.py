import queue
def rooms(list):
	q = queue.Queue()
	l=[False]*(len(list))
	l[0]=True
	for i in list[0]:
		q.put(i)
	while(q.qsize()!=0):
		i=q.get()
		# print(i)
		if(l[i]==False):
			l[i]=True
			for j in list[i]:
				if(j<len(list)):
					q.put(j)
	for i in l:
		if(i==False):
			return False
	return True


print(rooms([[1], [0,2], [3]]))
print(rooms([[1,3], [3,0,1], [2], [0]]))
print(rooms([[1,2,3], [0], [0], [0]]))
print(rooms([[1], [0,2,4], [1,3,4], [2], [1,2]]))
print(rooms([[1], [2,3], [1,2], [4], [1], [5]]))

print(rooms([[1], [2], [3], [4], [2]]))
print(rooms([[1], [1,3], [2], [2,4,6], [], [1,2,3], [1]]))
