def readData(data):
	inputList = list()
	with open(data) as f:		
		for line in f:	
			inputList.append(line.strip()) 			
	return inputList
	

dictNumber = {"zero" : 0, "one" : 1, "two" : 2 , "three" : 3 , "four" :4 , "five" : 5 , "six" : 6 , "seven" : 7 , "eight":8 , "nine" : 9}