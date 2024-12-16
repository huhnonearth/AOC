from sys import exit as SYSExit
from regex import findall as REFindall
from regex import match as REMatch
from regex import search as RESearch
from os.path import basename as OSPBasename
from math import prod as  MATHProd

def update_dict(rule_dict, key, value):
    
    if key in rule_dict.keys():
        rule_dict[key].add(value)
    else:       
        rule_dict[key] = {value}


    
    
def getResult(inputList, task):
    result = 0
    result2 = 0
    rule_dict = dict()
    update_list = list()
    for line in inputList:
        match = REFindall(r'(\d+\|\d+)', line)
        
        if match:
            tmp = match[0].split("|")
            update_dict(rule_dict, tmp[0], tmp[1])

        if "," in line:
            update_list.append(line)

    for ele in update_list:
        zeilen_list =  ele.split(",")
        len_zeilen_list = len(zeilen_list)
        merke_index = len_zeilen_list//2
        flag_page_number_valid = True
        for  i in range(1, len_zeilen_list):
            
            previous_page_numbers = set(zeilen_list[:i])
            
            set_values_of_dict = rule_dict[zeilen_list[i]] if zeilen_list[i] in rule_dict.keys() else set()
            
            if not previous_page_numbers.intersection(set_values_of_dict):
                continue
            flag_page_number_valid = False
            break
        if  flag_page_number_valid:
            result += int(zeilen_list[merke_index])
        else:
            
            # Erzeugung einer Vollordnung
            actual_rule_dict = dict()
            for key in rule_dict.keys():
                if key in ele:
                    actual_rule_dict[key] = set()
                    for set_ele in  rule_dict[key]:
                        if set_ele in  ele:
                            actual_rule_dict[key].add(set_ele)
            new_update_list = list()
            while actual_rule_dict:
                for key in  actual_rule_dict.keys():
                    flag_key_in_set = False
                    for val in  actual_rule_dict.values():
                        if key in val:
                            flag_key_in_set  = True
                            break
                    if not flag_key_in_set:
                        break
                new_update_list.append(key)
                del actual_rule_dict[key]
            
            result2 += int(new_update_list[merke_index])

    return result if task == 1 else result2

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
    print_me(task = 1, expected_result = 143, input_file = r'input_1.txt')
    print_me(task = 1, expected_result = 7198, input_file = r'input_2.txt')
    #print_me(task = 2, expected_result = 48, input_file = r'input_3.txt')
    print_me(task = 2, expected_result = 123, input_file = r'input_1.txt')
    print_me(task = 2, expected_result = 4230, input_file = r'input_2.txt')

if __name__ == "__main__":
    SYSExit(main())