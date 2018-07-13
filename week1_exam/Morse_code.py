def Morse(list):
	dict ={'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
	set1=set()
	for str in list:
		temp=""
		for i in str:
			temp+=dict[i]
		set1.add(temp)
	return len(set1)




print Morse(["gin", "zen", "gig", "msg"])
print Morse(["a", "z", "g", "m"])
print Morse(["bhi", "vsv", "sgh", "vbi"])
print Morse(["a", "b", "c", "d"])
print Morse(["hig", "sip", "pot"])
