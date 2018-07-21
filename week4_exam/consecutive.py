def consecutive(num):
	if(num==0):
		return 0
	binary = bin(num)[2:].strip()
	# print binary
	if num < 0:
	    limit = len('{0:b}'.format(num))
	    binary = ('{0:b}'.format(num + (1 << 32)))[-limit:]
	res = binary.split('1')[:-2]
	if(res==[]):
		return 0
	return max(len(str)+1 for str in res)

print consecutive(55)
print consecutive(-5)
print consecutive(0)
print consecutive(12354)
print consecutive(6)

print consecutive(256)
