#constants.
ASCENDING   = 0
DESCENDING  = 1

'''
The sort data function takes an unsorted list, an order value, and a category as parameters
then reorders the input list into a sorted list.
We use an merge sort, for this algorithm.
[IN]
unsorted_data - the unsorted list
order - flags if it is in ascending or descending order
category - integer representation of the category where we will search from

[OUT]
None, The unsorted data input parameter will be sorted 
'''
def MergeSort(unsorted_data, order, category):
    """Sort L."""
    
    # Make a list of 1-item lists so that we can start merging.
    workspace = []
    for i in range(len(unsorted_data)):
        workspace.append([unsorted_data[i]])
    
    # The next two lists to merge are workspace[i] and workspace[i + 1].
    i = 0
    
    # As long as there are at least two more lists to merge, merge them.
    while i < len(workspace) - 1:
        L1 = workspace[i]
        L2 = workspace[i + 1]
        newL = merge(L1, L2, order, category)
        workspace.append(newL)
        i += 2

    # Copy the result back into L.
    if len(workspace) != 0:
        unsorted_data[:] = workspace[-1][:]

def merge(L1, L2, order, category):
    """Merge sorted lists L1 and L2 and return the result."""
    
    newL = []
    i1 = 0
    i2 = 0

    # For each pair of items L1[1], L2[i2], copy the smaller into newL.
    while i1 != len(L1) and i2 != len(L2):
        if(order == ASCENDING):
            if L1[i1][category] <= L2[i2][category]:
                newL.append(L1[i1])
                i1 += 1
            else:
                newL.append(L2[i2])
                i2 += 1

        elif(order == DESCENDING):
            if L1[i1][category] >= L2[i2][category]:
                newL.append(L1[i1])
                i1 += 1
            else:
                newL.append(L2[i2])
                i2 += 1

        else:
            pass
    
    # Gather any leftover items from the two sections.
    # Note that one of them will be empty because of the loop condition.
    newL.extend(L1[i1:])
    newL.extend(L2[i2:])

    return newL