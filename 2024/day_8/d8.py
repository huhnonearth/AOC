from sys import exit as SYSExit
from regex import findall as REFindall
from regex import match as REMatch
from regex import search as RESearch
from os.path import basename as OSPBasename
from math import prod as  MATHProd
from math import gcd as MATHGcd

  
  
def getResult(inputList, task):
    result = 0
    antennen_dict = dict()
    tmp_rest_list = set()
    for i in range(len(inputList)):

        for  j in range(len(inputList[0])):
            ele = inputList[i][j]
            if ele != ".":
                if ele not in antennen_dict.keys():
                    antennen_dict[ele] =  [(i,j)]

                else:
                    antennen_dict[ele].append((i,j))


        
    for  key in antennen_dict.keys():

        for  value in antennen_dict.values():
            
            while value:
                tmp_tupel = value.pop()
            
                for ele in value:
                    if task == 2:
                        x_diff = tmp_tupel[0] - ele [0]
                        y_diff = tmp_tupel[1] - ele [1]
                        gcd = MATHGcd(x_diff, y_diff)
                        x_diff = x_diff / gcd
                        y_diff = y_diff / gcd
                        i = 0
                        while 0 <= tmp_tupel[0] + i *x_diff < len(inputList) and 0 <= tmp_tupel[1] + i * y_diff < len(inputList[0]):
                            tmp_rest_list.add((tmp_tupel[0] + i *x_diff , tmp_tupel[1] + i * y_diff) )
                            i += 1
                        i = 0
                        while 0 <= tmp_tupel[0] + i *x_diff < len(inputList) and 0 <= tmp_tupel[1] + i * y_diff < len(inputList[0]):
                            tmp_rest_list.add((tmp_tupel[0] + i *x_diff , tmp_tupel[1] + i * y_diff) )
                            i -= 1
                    if task == 1:
                        ON1 = (2*tmp_tupel[0] - ele[0], 2*tmp_tupel[1] - ele[1]) 
                        ON2 = (-tmp_tupel[0] + 2 * ele[0], - tmp_tupel[1] + 2 * ele[1]) 
                        
                        if ON1[0] >= 0 and ON1[1] >= 0 and  ON1[0] < len(inputList) and ON1[1] < len(inputList[0]) :
                            tmp_rest_list.add(ON1) 
                        if ON2[0] >= 0 and ON2[1] >= 0 and   ON2[0] < len(inputList) and ON2[1] < len(inputList[0]):
                            tmp_rest_list.add(ON2) 
                
    print(tmp_rest_list)


           
        
      

    return len(tmp_rest_list)

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
    print_me(task = 1, expected_result = 14, input_file = r'input_1.txt')
    print_me(task = 1, expected_result = 303, input_file = r'input_2.txt')
    #print_me(task = 2, expected_result = 48, input_file = r'input_3.txt')
    print_me(task = 2, expected_result = 34, input_file = r'input_1.txt')
    print_me(task = 2, expected_result = 34, input_file = r'input_2.txt')

if __name__ == "__main__":
    SYSExit(main())