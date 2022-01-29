#####################################
#           CMSC11: LAB 10          #
#   Prepared by: Gregory Parcon     #
#####################################
import time                                     #used for clocking running time.
from datetime import datetime                   #used for processing the birthday.

#import the searching and sorting modules.
from LinearSearch import LinearSearch
from BinarySearch import BinarySearch
from InsertionSort import InsertionSort
from SelectionSort import SelectionSort
from MergeSort import MergeSort

#constants.
DIVIDER     = "==================================="
HEIGHT_UNIT = 'cm'
WEIGHT_UNIT = 'kg'
NANOSECOND  = (10 ** 9)

ASCENDING   = 0
DESCENDING  = 1

#Will be used for indexing of the array.
NAME        = 0
POSITION    = 1
TEAM        = 2
BIRTHDAY    = 3
HEIGHT      = 4
WEIGHT      = 5

'''
The PrintSearchResult function takes a list as an arguement
and prints the contents of the list on the console.
It has no return value.

[IN]
result_list - the result list of the search algorithm.

[OUT]
None
'''
def PrintSearchResult(result_list):
    print("\nSearch results : ")

    #if there are elements on the list, print the contents.
    if(len(result_list) != 0):

        '''Return the data in its original state (same as the input text file)'''
        for item in result_list:
            for i in range(len(item)):
                if(i == BIRTHDAY):
                    print(item[i].strftime('%Y/%m/%d'))
                
                elif(i == HEIGHT):
                    print(str(item[i]) + HEIGHT_UNIT, end ="/")

                elif(i == WEIGHT):
                    print(str(item[i]) + WEIGHT_UNIT)

                else:
                    print(item[i])
            print("")                               #print a new line

    #if search result is empty, print "Not found".
    else:
        print("Not found")

'''
The CreateSortedResult function takes a sorted list as an arguement
and concatenates the contents of the list into one string and return that string.

[IN]
result_list - the result list of the search algorithm.

[OUT]
sorted_data - concatenated string
'''
def CreateSortedResult(result_list):
    
    sorted_data = "\n"                          #String to concatenate all data

    '''Return the data in its original state (same as the input text file)'''
    for item in result_list:
        for i in range(len(item)):
            if(i == BIRTHDAY):
                sorted_data += item[i].strftime('%Y/%m/%d')
                
            elif(i == HEIGHT):
                sorted_data += str(item[i]) + HEIGHT_UNIT + "/"

            elif(i == WEIGHT):
               sorted_data += str(item[i]) + WEIGHT_UNIT

            else:
                sorted_data += item[i]
            sorted_data += "\n"                    #new line.
        sorted_data += "\n"                        #new line.

    return sorted_data


'''Main function where the bulk of processing happens'''
def main():
    f = open("nippon_vbt.txt", "r")                 #opens the text file.

    raw_data = f.read().split('\n')                 #reads the content and splits it line by line.

    f.close()                                       #closes the file after reading the content.

    '''
    build your table (2-dimensional array).
    This time, we use a list as our data structure.
    [[player1name, position, team, birthday, height, weight],
    [player2name, position, team, birthday, height, weight],
    ...]
    We declared two lists, one for the bigger array - team data.
    another to hold each individual data which will be added to the team data.
    '''
    team_data = list()
    player_data = list()

    for i in raw_data:
        player_data.append(i)                       #appends each element to the player data.

        '''if we see an empty string which represents the space in between the player data in the text file,
        we process player_data, add it to the team_data list and resets the player_data list to empty again
        in order to process the next batch.'''
        if(i == ''):
            player_data.pop()                       #removes the last element which is the ''.

            stats = player_data.pop().split('/')    #removes the height and weight data for processing.

            str_birthday = player_data.pop()        #removes the birthday data for procesing.

            #converts the string birthday into datetime format.
            birthday = datetime.strptime(str_birthday, '%Y/%m/%d')

            '''removes the unit at the end of each string 
            and converts the height and weight into integer values.'''
            height = stats[0]
            height = int(height[:-2])
            weight = stats[1]
            weight = int(weight[:-2])

            #return the processed data back to the player_data list in the correct order.
            player_data.append(birthday)
            player_data.append(height)
            player_data.append(weight)
            
            team_data.append(player_data)
            player_data = []
        else:
            pass

    #ask if the user wants to search or sort.
    mode = int(input("1. Search\n2. Sort\nEnter the mode : "))

    #ask the category from which the user wants to search/sort.
    category = int(input("1. Name\n2. Position\n3. Current team\n4. Birthday (yyyy/mm/dd)\n5. Height (cm)\n6. Weight (kg)\nEnter the category : "))
    category = category-1                       #Adjust the category value for indexing

    #user chooses to search.
    if mode == 1:
        #ask the user the value it wants to search.
        value = str(input("Search value : "))

        #convert the birthday into datetime format.
        if(category == BIRTHDAY):
            value = datetime.strptime(value, '%Y/%m/%d')

        #convert the height and weight into integer format.
        elif(category == HEIGHT or category == WEIGHT):
            value = int(value)

        #otherwise, value remains a string.
        else:
            pass

        '''perform linear search and clock the running time before and after function call.
        you may also opt to clock your algorithms within their respective modules
        as long as the whole process is covered.'''
        print("\nLINEAR SEARCH")
        init_time = time.perf_counter()             #get the start time

        '''Call the linear search algorithm.
        assign the result to a new array'''
        linear_result = LinearSearch(team_data,category,value)
        
        fin_time = time.perf_counter()              #get the end time
        
        linear_time = fin_time - init_time          #get the time difference

        PrintSearchResult(linear_result)
        
        print("Linear Search Running time : ", round(linear_time,9))

        '''perform binary search and clock the running time before and after function call.
        you may also opt to clock your algorithms within their respective modules
        as long as the whole process is covered.'''
        print("\nBINARY SEARCH")

        '''Sort the team_data list in ascending order for this example.
        However, you can choose to sort in descnding order, but the binary search algorithm must be adjusted as well.'''
        InsertionSort(team_data, ASCENDING, category)

        init_time = time.perf_counter()             #get the start time

        #Call the linear search algorithm then assign the result to a new array
        binary_result = BinarySearch(team_data,category,value)

        fin_time = time.perf_counter()              #get the end time
        
        binary_time = fin_time - init_time          #get the time difference
        
        PrintSearchResult(binary_result)
        print("Binary Search Running time : ", round(binary_time,9))

    if(mode == 2):
        #ask the sorting order from the user.
        order = int(input("1. Ascending\n2. Descending\nEnter the order : "))
        order = order-1                       #Adjust the order value for indexing

        #Assign the team_data into three new lists for the three sorting algorithms.
        insertion_list, selection_list, merge_list = team_data, team_data, team_data

        '''perform Insertion sort and clock the running time before and after function call.
        you may also opt to clock your algorithms within their respective modules
        as long as the whole process is covered.'''
        print("\nINSERTION SORT")
        init_time = time.perf_counter()             #get the start time

        #Call the insertion sort algorithm.
        InsertionSort(insertion_list, order, category)
        
        fin_time = time.perf_counter()              #get the end time
        
        insertion_time = fin_time - init_time       #get the time difference
        
        print("Insertion Sort Running time : ", round(insertion_time,9))

        '''perform Selection sort and clock the running time before and after function call.
        you may also opt to clock your algorithms within their respective modules
        as long as the whole process is covered.'''
        print("\nSELECTION SORT")
        init_time = time.perf_counter()             #get the start time

        #Call the insertion sort algorithm.
        SelectionSort(selection_list, order, category)
        
        fin_time = time.perf_counter()              #get the end time
        
        selection_time = fin_time - init_time       #get the time difference

        #PrintSearchResult(insertion_list)
        
        print("Selection Sort Running time : ", round(selection_time,9))

        '''perform Merge sort and clock the running time before and after function call.
        you may also opt to clock your algorithms within their respective modules
        as long as the whole process is covered.'''
        print("\nMERGE SORT")
        init_time = time.perf_counter()             #get the start time

        #Call the insertion sort algorithm.
        MergeSort(merge_list, order, category)
        
        fin_time = time.perf_counter()              #get the end time
        
        merge_time = fin_time - init_time       #get the time difference

        #PrintSearchResult(insertion_list)
        print("Merge Sort Running time : ", round(merge_time,9))

        #write sorted data into the file.
        write_data = ""
        write_data = write_data + "SELECTION SORT\n" + DIVIDER + CreateSortedResult(selection_list)
        write_data = write_data + "INSERTION SORT\n" + DIVIDER + CreateSortedResult(insertion_list)
        write_data = write_data + "MERGE SORT\n" + DIVIDER + CreateSortedResult(merge_list)


        fw = open("sorted_nippon_vbt.txt", "w")
        fw.write(write_data)
        fw.close()

#call the main function.
main()