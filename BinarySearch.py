#Will be used for indexing of the array.
NAME      = 0
POSITION  = 1
TEAM      = 2
BIRTHDAY  = 3
HEIGHT    = 4
WEIGHT    = 5

'''
The Binary Search function takes 3 arguements and returns a list:
[IN]
team_data - the team data list where we will do the search
category - integer representation of the category where we will search from
value - the item being searched

[OUT]
return_list = return the result of the seach in a list
'''
def BinarySearch(team_data, category, value):
    return_list = []
    
    #define the first and last indices. Endpoints of your list.
    first = 0
    last = len(team_data) - 1

    while first != last + 1:
        #We get the median index using integer division.
        median = (first + last)//2

        #in cases where the item being searched is a string, casefold() is used to make search case insensitive.
        if(category == NAME or category == TEAM or category == POSITION):
        
            '''If the value of the middle index is greater than the search value,
            Set the last index as the middle to cut the list into the first half.'''
            if(team_data[median][category].casefold() > value.casefold()):
                last = median - 1

            #If the value of the middle index is less than the search value,
            #Set the first index as the middle to cut the list into the second half.
            elif(team_data[median][category].casefold() < value.casefold()):
                first = median + 1

            #If the value of the middle index is equal to the search value,
            #Add the the item to the return list, remove it from the sorted data
            #and reset the first and last indices to search again in case of duplicates
            elif(team_data[median][category].casefold() == value.casefold()):
                return_list.append(team_data[median])
                team_data.pop(median)
                first = 0
                last = len(team_data) - 1

            #Otherwise, break from the loop.
            else:
                break

        #Same logic as above but handles data other than strings.
        else:
            '''If the value of the middle index is greater than the search value,
            Set the last index as the middle to cut the list into the first half.'''
            if(team_data[median][category] > value):
                last = median - 1

            #If the value of the middle index is less than the search value,
            #Set the first index as the middle to cut the list into the second half.
            elif(team_data[median][category] < value):
                first = median + 1

            #If the value of the middle index is equal to the search value,
            #Add the the item to the return list, remove it from the sorted data
            #and reset the first and last indices to search again in case of duplicates
            elif(team_data[median][category] == value):
                return_list.append(team_data[median])
                team_data.pop(median)
                first = 0
                last = len(team_data) - 1

            #Otherwise, break from the loop.
            else:
                break

    return return_list

