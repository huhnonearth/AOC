from sys import exit as SYSExit
from regex import findall as REFindall
from regex import match as REMatch
from regex import search as RESearch
from os.path import basename as OSPBasename
from math import prod as  MATHProd


def getResult(inputList, task):
    
    result = 0
    do_flag = True
    for line in inputList:  
        if task == 1:      
            result += sum(map(lambda x: MATHProd(map(int , REFindall( r'\d+' , x))), REFindall( r'mul\(\d+,\d+\)' ,line)))
        if task  == 2:
            tmp = REFindall( r"mul\(\d+,\d+\)|don't\(\)|do\(\)", line)
            
            for ele in tmp:
                if ele == "don't()":
                    do_flag = False
                elif ele == "do()":
                    do_flag = True
                else:
                    if do_flag:
                        result += MATHProd(map(int , REFindall( r'\d+' , ele)))

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
    print_me(task = 1, expected_result = 161, input_file = r'input_1.txt')
    print_me(task = 1, expected_result = 167650499, input_file = r'input_2.txt')
    print_me(task = 2, expected_result = 48, input_file = r'input_3.txt')
    #print_me(task = 2, expected_result = 4, input_file = r'input_1.txt')
    print_me(task = 2, expected_result = 95846796, input_file = r'input_2.txt')

if __name__ == "__main__":
    SYSExit(main())