def mostCommonName(L):
	d = dict()
	maxValue = 0
	mostCommonName = set()
	if len(L) == 0: return None
	for i in L:
		if d.get(i,0) == 0:
			d[i] = 1
		else:
			d[i] +=1
	for i in L:
		if d[i] >= maxValue:
			maxValue = d[i]
	for i in d:
		if d[i] == maxValue:
			mostCommonName.add(i)
	return mostCommonName


def testMostCommonName():
	print("Testing mostCommonName()...", end="")
	assert(mostCommonName(["Jane", "Aaron", "Cindy", "Aaron"]) == {"Aaron"})
	assert(mostCommonName(["Jane", "Aaron", "Jane", "Cindy", "Aaron"]) == {"Aaron", "Jane"})
	assert(mostCommonName(["Cindy"]) == {"Cindy"})
	assert(mostCommonName(["Jane", "Aaron", "Cindy"]) == {"Aaron", "Cindy", "Jane"})
	assert(mostCommonName([]) == None)
	print("Passed!")

testMostCommonName()




def getPairSum(L,target):
	l = []
	for i in range(len(L)):
		for j in range(i+1,len(L)):
			if L[i] + L[j] == target:
				l.append((L[i],L[j]))
				if L[i] != L[j]:
					l.append((L[j],L[i]))
	return l


def testGetPairSum():
	print("Testing getPairSum()...", end="")
	assert(getPairSum([1], 1) == [])
	assert(getPairSum([10, -1, 1, -8, 3, 1], 10) == [])
	assert(getPairSum([5,2],7)==[(5,2),(2,5)])
	print("Passed!")
testGetPairSum()

