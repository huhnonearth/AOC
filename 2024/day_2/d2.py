from sys import exit as SYSExit
from regex import findall as REFindall
from regex import match as REMatch
from regex import search as RESearch
from os.path import basename as OSPBasename


def getResult(inputList, task):
    read_list_1 = list()

    result = 0
    for line in inputList:
        read_list_1 = list(map(int, REFindall( r'\d+' ,line)))
        
        if task == 1:
            res_up  = all(i < j for i, j in zip(read_list_1, read_list_1[1:]))
            res_down  = all(i > j for i, j in zip(read_list_1, read_list_1[1:]))
            res_diff = all( abs(i - j) <= 3 for i, j in zip(read_list_1, read_list_1[1:]))
        
            if (res_up or res_down) and res_diff:
                result += 1
                
        if task == 2:
            for i in range(len(read_list_1)):
                read_list_2 = read_list_1.copy()
                del read_list_2[i]
                res_up  = all(i < j for i, j in zip(read_list_2, read_list_2[1:]))
                res_down  = all(i > j for i, j in zip(read_list_2, read_list_2[1:]))
                res_diff = all( abs(i - j) <= 3 for i, j in zip(read_list_2, read_list_2[1:]))
                
                if (res_up or res_down) and res_diff:
                    result += 1
                    break           
            
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
    print_me(task = 1, expected_result = 2, input_file = r'input_1.txt')
    print_me(task = 1, expected_result = 686, input_file = r'input_2.txt')
    print_me(task = 2, expected_result = 4, input_file = r'input_1.txt')
    print_me(task = 2, expected_result = 0, input_file = r'input_2.txt')

if __name__ == "__main__":
    SYSExit(main())