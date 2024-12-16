from sys import exit as SYSExit
from regex import findall as REFindall
from regex import match as REMatch
from regex import search as RESearch
from os.path import basename as OSPBasename
from math import prod as  MATHProd


def is_valid(matches, task):
    if len(matches) == 2:
        return matches[0] == matches[1]
    if matches[0] % matches[-1] == 0:

        if is_valid([matches[0] // matches[-1] ]+ matches[1:-1], task):
            return True
    if task == 2:
        if len(str(matches[0])) > len(str(matches[-1])):
            if str(matches[0])[-len(str(matches[-1])):] == str(matches[-1]):
                if is_valid([int(str(matches[0])[:-len(str(matches[-1]))]) ]+  matches[1:-1], task):
                    return True
    if matches[0] - matches[-1] > 0:
        if is_valid([matches[0] - matches[-1] ] +  matches[1:-1], task): 
            return True
    

    return False   
  
def getResult(inputList, task):
    result = 0
    
    for line in inputList:
        matches = list(map(int , REFindall( r'\d+', line)))

        result += matches[0] if is_valid(matches, task) else 0
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
    print_me(task = 1, expected_result = 3749, input_file = r'input_1.txt')
    print_me(task = 1, expected_result = 3245122495150, input_file = r'input_2.txt')
    #print_me(task = 2, expected_result = 48, input_file = r'input_3.txt')
    print_me(task = 2, expected_result = 11387, input_file = r'input_1.txt')
    print_me(task = 2, expected_result = 105517128211543, input_file = r'input_2.txt')

if __name__ == "__main__":
    SYSExit(main())