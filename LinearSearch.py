#Will be used for indexing of the array.
NAME      = 0
POSITION  = 1
TEAM      = 2
BIRTHDAY  = 3
HEIGHT    = 4
WEIGHT    = 5

'''
The Linear Search function takes 3 arguements and returns a list:
[IN]
team_data - the team data list where we will do the search
category - integer representation of the category where we will search from
value - the item being searched

[OUT]
return_list = return the result of the seach in a list
'''

def LinearSearch(team_data, category, value):
  return_list = []
  for item in team_data:
    '''in cases where the item being searched is a string, we apply casefold to make it case insensitive
    if a substring of the value is found, add the item to the return list.'''
    if(category == NAME or category == TEAM or category == POSITION):
      if(item[category].casefold() == value.casefold()):
        return_list.append(item)
      else:
        pass

    #if category is not a string, simply check for equal values.
    else:
      if(item[category] == value):
        return_list.append(item)
      else:
        pass
  return return_list