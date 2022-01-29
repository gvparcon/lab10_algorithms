#constants.
ASCENDING   = 0
DESCENDING  = 1

'''
The sort data function takes an unsorted list, an order value, and a category as parameters
then reorders the input list into a sorted list.
We use an insertion sort, for this algorithm.
[IN]
unsorted_data - the unsorted list
order - flags if it is in ascending or descending order
category - integer representation of the category where we will search from

[OUT]
None, The unsorted data input parameter will be sorted 
'''
def InsertionSort(unsorted_data, order, category):
    """Reorder the values in L from smallest to largest."""

    i = 0
    while i != len(unsorted_data):
        insert(unsorted_data, i, order, category)
        i = i + 1

def insert(L, b, order, category):
    """Insert L[b] where it belongs in L[0:b + 1]; 
       L[0:b - 1] must already be sorted."""

    # Find where to insert L[b] by searching backwards from L[b] for a smaller item.
    i = b
    if(order == ASCENDING):
        while i != 0 and L[i - 1][category] >= L[b][category]:
            i = i - 1

        # Move L[b] to index i, shifting the following values to the right.
        value = L[b]
        del L[b]
        L.insert(i, value)

    elif(order == DESCENDING):
        while i != 0 and L[i - 1][category] <= L[b][category]:
            i = i - 1

        # Move L[b] to index i, shifting the following values to the right.
        value = L[b]
        del L[b]
        L.insert(i, value)

    else:
        pass