from sys import exit as SYSExit
from regex import findall as REFindall
from regex import match as REMatch
from regex import search as RESearch
from os.path import basename as OSPBasename
from math import prod as  MATHProd


def getResult(inputList, task):
    
    result = 0
    
    line_length = len(inputList)
    r = line_length + len( inputList[0] )
    inputList.append("      ")
    for i in range(len( inputList[0] )):
        row_list = list()
        for j in range(line_length):  
            row_list.append(list(inputList[j])[i])
        inputList.append(''.join(row_list))
    inputList.append("      ")    
    for k in range(r-1):
        leftIndex = max(0, k - line_length + 1)
        rightIndex =  min(k, len( inputList[0] ) - 1)
        row_list = list()
        for column_index in range(leftIndex, rightIndex + 1):  
            row_list.append(list(inputList[k-column_index])[column_index])
        inputList.append(''.join(row_list))
    inputList.append("      ")    
                
    for k in range(r-1):
        leftIndex = max(0, k - line_length + 1)
        rightIndex =  min(k, len( inputList[0] ) - 1)
        row_list = list()    
        
        for column_index in range(leftIndex, rightIndex + 1):  
            row_list.append(list(inputList[line_length - k - 1 +column_index])[column_index])
        inputList.append(''.join(row_list))



    for line in inputList:
        match = REFindall(r'XMAS' , line) 
        match2 =  REFindall(r'SAMX' , line)        
        result += (len(match) + len(match2))
    
    
    resultzwei = 0
    
    
    for i in range(1, line_length - 1):
        for j in range(1, len(inputList[i]) - 1):
            if  inputList[i][j] != 'A':
                continue
            li_o = inputList[i-1][j-1]
            re_o = inputList[i-1][j+1]
            li_u = inputList[i+1][j-1]
            re_u = inputList[i+1][j+1]
            
            if ((li_o == "M" and re_u == "S") or (li_o == "S" and re_u == "M")) and ((re_o == "M" and li_u == "S") or (re_o == "S" and li_u == "M")):
                resultzwei += 1

    return result if task == 1 else resultzwei

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
    print_me(task = 1, expected_result = 18, input_file = r'input_1.txt')
    print_me(task = 1, expected_result = 2557, input_file = r'input_2.txt')
    #print_me(task = 2, expected_result = 48, input_file = r'input_3.txt')
    print_me(task = 2, expected_result = 9, input_file = r'input_1.txt')
    print_me(task = 2, expected_result = 0, input_file = r'input_2.txt')

if __name__ == "__main__":
    SYSExit(main())