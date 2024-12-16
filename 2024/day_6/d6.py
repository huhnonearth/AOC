from sys import exit as SYSExit
from regex import findall as REFindall
from regex import match as REMatch
from regex import search as RESearch
from os.path import basename as OSPBasename
from math import prod as  MATHProd

pfeile = ["^", ">", "v", "<"]

def loop_checker(inputList, reihe, spalte, laufrichtung):
    debugg = False
    bool_val = False
    position = inputList[reihe][spalte]
    position_x_for_raute_reihe = -1
    position_x_for_raute_spalte = -1
    dict_of_positions = dict()


    if laufrichtung % 4 == 0:
        position_x_for_raute_reihe = reihe -1
        position_x_for_raute_spalte = spalte
    if laufrichtung % 4 == 1:
        position_x_for_raute_spalte = spalte +1
        position_x_for_raute_reihe = reihe
    if laufrichtung % 4 == 2:
        position_x_for_raute_reihe = reihe +1 
        position_x_for_raute_spalte = spalte 
    if laufrichtung % 4 == 3:
        position_x_for_raute_spalte = spalte -1
        position_x_for_raute_reihe = reihe
        
            
    while (reihe not in dict_of_positions.keys()) or (spalte not in dict_of_positions[reihe].keys()) or ((laufrichtung % 4) not in dict_of_positions[reihe][spalte]):

        if reihe not in dict_of_positions.keys():
            dict_of_positions[reihe] = dict()
        if spalte not in  dict_of_positions[reihe].keys():
            dict_of_positions[reihe][spalte] = set()
        dict_of_positions[reihe][spalte].add( laufrichtung %  4 )
        
        if not(0 < reihe < len(inputList)-1 and 0 < spalte < len(inputList[0])-1):

            return False
        
        laufrichtung += 1
        
        if laufrichtung % 4 == 0:
            weg_list = list(map( lambda x: inputList[x][spalte], range(reihe-1, -1, -1)))
            weg_list.append("#")
            
            if spalte == position_x_for_raute_spalte:
                if position_x_for_raute_reihe < reihe:
                    weg_list[reihe  - position_x_for_raute_reihe -1] = "#"

            raute_index = weg_list.index(("#"))
            reihe = reihe - raute_index
        if laufrichtung % len(pfeile) == 1:
            weg_list = list(map( lambda x: inputList[reihe][x], range(spalte+1,  len(inputList[0]))))
            weg_list.append("#")
            
            if reihe == position_x_for_raute_reihe:
                if position_x_for_raute_spalte > spalte:
                    weg_list[position_x_for_raute_spalte  - spalte -1] = "#"
            raute_index = weg_list.index(("#"))
            spalte = spalte  + raute_index

        if laufrichtung % len(pfeile) == 2:

            weg_list = list(map( lambda x: inputList[x][spalte], range(reihe+1,  len(inputList))))
            weg_list.append("#")
            
            if spalte == position_x_for_raute_spalte:
                if position_x_for_raute_reihe > reihe:
                    weg_list[position_x_for_raute_reihe - reihe  -1] = "#"
            
            raute_index = weg_list.index(("#"))
            reihe = reihe + raute_index

        if laufrichtung % len(pfeile) == 3:
            weg_list = list(map( lambda x: inputList[reihe][x], range(spalte-1, -1, -1)))
            weg_list.append("#")
            
            if reihe == position_x_for_raute_reihe:
                if position_x_for_raute_spalte < spalte:
                    weg_list[spalte - position_x_for_raute_spalte -1] = "#"
            
            raute_index = weg_list.index(("#"))
            spalte = spalte  - raute_index

    return True
    
  
def getResult(inputList, task):
    result = 0
    pfeil = "."
    weg_list = list()
    

     # Task 1
    inputList =  list(map( list, inputList))
    for reihe in range(len(inputList)):
        for spalte  in range(len(inputList[0])):
            ele = inputList[reihe][spalte]
            if ele != "."  and ele!= "#":
                pfeil  = ele
                inputList[reihe][spalte] = "X" 
                break
        if pfeil !=".":
            break

    result = 1   
   
    pfeileindex = pfeile.index(pfeil)
    result2 = 0
    while 0 < reihe < len(inputList)-1 and 0 < spalte < len(inputList[0])-1:


        if pfeileindex % len(pfeile) == 0:

            weg_list = list(map( lambda x: inputList[x][spalte], range(reihe-1, -1, -1)))
            weg_list.append("#")
            raute_index = weg_list.index(("#"))
            reihe = reihe - raute_index
            
            #pfeileindex += 1
            result += weg_list[:raute_index].count(".")
            for i in  range(raute_index):
                if inputList[reihe+i][spalte] != "X":
                    inputList[reihe+i] [spalte] = "X"
                    if task == 2:
                        if loop_checker(inputList, reihe+i+1, spalte, pfeileindex):
                            result2 += 1
                        
        if pfeileindex % len(pfeile) == 1:
            weg_list = list(map( lambda x: inputList[reihe][x], range(spalte+1,  len(inputList[0]))))
            weg_list.append("#")
            raute_index = weg_list.index(("#"))
            spalte = spalte  + raute_index
            
            #pfeileindex += 1
            result += weg_list[:raute_index].count(".")
            for i in  range(raute_index):
                if inputList[reihe][spalte-i] != "X":
                    inputList[reihe] [spalte-i] = "X"
                    if task == 2:
                        if loop_checker(inputList, reihe, spalte-i-1, pfeileindex):
                            result2 += 1
        if pfeileindex % len(pfeile) == 2:

            weg_list = list(map( lambda x: inputList[x][spalte], range(reihe+1,  len(inputList))))
            weg_list.append("#")
            raute_index = weg_list.index(("#"))
            reihe = reihe + raute_index
            
            #pfeileindex += 1
            result += weg_list[:raute_index].count(".")
            for i in  range(raute_index):

                if inputList[reihe-i][spalte] != "X":
                    inputList[reihe-i] [spalte] = "X" 
                    if task == 2:
                        if loop_checker(inputList, reihe-i-1, spalte, pfeileindex):
                            result2 += 1           
        if pfeileindex % len(pfeile) == 3:

            weg_list = list(map( lambda x: inputList[reihe][x], range(spalte-1, -1, -1)))
            weg_list.append("#")
            raute_index = weg_list.index(("#"))
            spalte = spalte  - raute_index
            
            #pfeileindex += 1
            result += weg_list[:raute_index].count(".")
            for i in  range(raute_index):
                if inputList[reihe][spalte+i] != "X":
                    inputList[reihe] [spalte+i] = "X"            
                    if task == 2:
                        if loop_checker(inputList, reihe, spalte+i+1, pfeileindex):
                            result2 += 1            
            
        pfeileindex += 1   



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
    print_me(task = 1, expected_result = 41, input_file = r'input_1.txt')
    print_me(task = 1, expected_result = 5305, input_file = r'input_2.txt')
    #print_me(task = 2, expected_result = 48, input_file = r'input_3.txt')
    print_me(task = 2, expected_result = 6, input_file = r'input_1.txt')
    print_me(task = 2, expected_result = 2143, input_file = r'input_2.txt')

if __name__ == "__main__":
    SYSExit(main())