from sys import exit as SYSExit
from regex import findall as REFindall
from regex import match as REMatch
from regex import search as RESearch
from os.path import basename as OSPBasename


def getResult(inputList, task):
    read_list_1 = list()
    read_list_2 = list()
    result = 0
    for line in inputList:
        matches = REFindall( r'\d+' ,line) 
        read_list_1.append(int(matches[0]))
        read_list_2.append(int(matches[1]))

    read_list_1.sort()
    read_list_2.sort()

    if task == 1:
        for i in range(len(read_list_1)):
            result += abs( read_list_1[i] - read_list_2[i])

    if task == 2:
        for ele in read_list_1:
            result += ele * read_list_2.count(ele)

    return result

def readData(data):
	inputList = list()
	with open(data) as f:		
		for line in f:	
			inputList.append(line.strip()) 			
	return inputList

def print_me(task, expected_result, input_file):
    inputList = readData(input_file)
    computed_result = getResult(inputList, task)
    tag = RESearch(r'd(\d+)\.py',  OSPBasename(__file__)).group(1)
    print( f"Day {tag} - Task {task} Inputfile {input_file}:\n\tExpected: {expected_result}\n\tGot: {computed_result}\n" )


def main():
    print_me(task = 1, expected_result = 11, input_file = r'input_1.txt')
    print_me(task = 1, expected_result = 3714264, input_file = r'input_2.txt')
    print_me(task = 2, expected_result = 31, input_file = r'input_1.txt')
    print_me(task = 2, expected_result = 18805872, input_file = r'input_2.txt')

if __name__ == "__main__":
    SYSExit(main())