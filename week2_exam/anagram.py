def anagram(string1,string2):
	l=[0]*26
	string1 = string1.lower()
	string2 = string2.lower()
	for i in string1:
		if(i.isalpha()):
			l[97-ord(i)]+=1

	for i in string2:
		if(i.isalpha()):
			l[97-ord(i)]-=1
	for i in l:
		if(i==-1):
			return False
	return True





print anagram("Mother In Law","Hitler Woman")
print anagram("anagram", "nagaram")
print anagram("Keep","Peek")
print anagram("School Master","The Classroom")
print anagram("ASTRONOMERS", "NO MORE STARS")
print anagram("Toss", "Shot")
print anagram("joy", "enjoy")
print anagram("Debit Card","Bad Credit")
print anagram("SiLeNt CAT", "LisTen AcT")
print anagram("Dormitory", "Dirty Room")

