#constants.
ASCENDING   = 0
DESCENDING  = 1

'''
The sort data function takes an unsorted list, an order value, and a category as parameters
then reorders the input list into a sorted list.
We use an selection sort, for this algorithm.
[IN]
unsorted_data - the unsorted list
order - flags if it is in ascending or descending order
category - integer representation of the category where we will search from

[OUT]
None, The unsorted data input parameter will be sorted 
'''
def SelectionSort(unsorted_data, order, category):
    """Reorder the values in unsorted_data."""

    i = 0
    while i != len(unsorted_data):
        extreme = find_extremes(unsorted_data, i, order, category)
        unsorted_data[i], unsorted_data[extreme] = unsorted_data[extreme], unsorted_data[i]
        i = i + 1

def find_extremes(L, b, order, category):
    """Return the index of the extreme value in L[b:]. Depending on the order."""

    extreme = b # The index of the extreme so far.
    i = b + 1
    while i != len(L):
        if(order == ASCENDING):
            if L[i][category] < L[extreme][category]:
                # We found a smaller item at L[i].
                extreme = i
            i = i + 1

        elif(order == DESCENDING):
            if L[i][category] > L[extreme][category]:
                # We found a larger item at L[i].
                extreme = i
            i = i + 1

        else:
            pass

    return extreme