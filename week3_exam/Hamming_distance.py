def binary(num):
	x=""
	while(num>0):
		x=str(num%2)+x
		num = num/2
	return x

def Hamming_distance(num1,num2):
	str1=binary(num1)
	str2=binary(num2)
	count= 0
	if(len(str1)>len(str2)):
		temp=len(str1)-len(str2)
		for i in range(temp):
			str2='0'+str2
	elif(len(str2)>len(str1)):
		temp=len(str2)-len(str1)
		for i in range(temp):
			str1='0'+str1
	for i in range(len(str1)):
		if(str1[i]!=str2[i]):
			count+=1
	return count


print Hamming_distance(1,4)
print Hamming_distance(25,30)
print Hamming_distance(100,250)
print Hamming_distance(1,30)
print Hamming_distance(0,255)