"""
In-class exercise: Implement the counting inversions algorithm
Group Members: Uchenna Obi, Samuel Hsiao
"""

def count_inversions(lst):
    """Returns the number of inversions.

    The list gets sorted as a side-effect

    Args:
        lst (list[int]): list of integers
        ant : is an array that will store the sorted numbers
    """ 
    if len(lst) <= 1 :
       return lst, 0 # 1 element no, inversions. Also when to end the recursion
    else:
     mid = len(lst) // 2 
     left_half, left_inv = count_inversions(lst[:mid])  
     right_half, right_inv = count_inversions(lst[mid:])
     ant, cross_inv =merge(left_half, right_half) # use the merge function below to sort and count the cross inversions and store int in ant
     return  ant , left_inv + right_inv + cross_inv
    

def merge(left, right):
    """Returns a merged, sorted list and a count of
    cross-inversions.

    The lists left and right differ in length by at most 1.
    and are already sorted. A cross-inversion is an instance
    of x in left and y in right such that x > y.

    Args:
        left (list[int]): sorted list
        right (list[int]): sorted list
    """
    ant = []
    cross_inv = 0
    i, j  = 0, 0
    while i != len(left) and j != len(right):
      if left[i] > right[j]:
        ant.append(right[j])
        j += 1
        cross_inv += len(left) -i# this counts the split inversion when the indexes on the left array and bigger than the right array
      else:
        ant.append(left[i])
        i += 1
    ant = ant + left[i:] + right[j:]
    return ant, cross_inv
    
    


lst = [1,3,5,2,4,6]
print("Number of inversions for the list are", count_inversions(lst))
lst = [4,3,2,1,]
print("Number of inversions for the list are", count_inversions(lst))