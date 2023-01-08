import matplotlib.pyplot as plt

# Assigns the jth element in the old_list to the ith element in the new_list 
def assigment(new_list, i, old_list, j):
    new_list[i] = old_list[j]


def merge_sort(list_to_sort_by_merge):
    if len(list_to_sort_by_merge) > 1:
        
        
        # We define the outer limits and the middle part of the list
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        l = 0 # Initial length of first subarray
        r = 0 # Initial length of second subarray
        i = 0 # Counter variable for the loops

        merge_sort(left)
        merge_sort(right)
        
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                assigment(new_list=list_to_sort_by_merge, i=i, old_list=left, j=l)
                l += 1
            else:
                assigment(new_list=list_to_sort_by_merge, i=i, old_list=right, j=r)
                r += 1
            i += 1

        # Copy the remaining elements of left[l], if there are any
        while l < len(left):
            list_to_sort_by_merge[i] = left[l]
            l += 1
            i += 1

        # Copy the remaining elements of right[r], if there are any
        while r < len(right):
            list_to_sort_by_merge[i] = right[r]
            r += 1
            i += 1



# Create a list full of numbers with two decimals each
my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Plot before the mergeSort function has been called
x = range(len(my_list)) # saves the length of the list as a range in the variable "x"
plt.plot(x, my_list) # uses the range and the elements of my_list to create a plot
plt.show() # displays the plot

# Calling the merge_sort function
merge_sort(my_list)

# Plot after the merge_sort function has been called
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
