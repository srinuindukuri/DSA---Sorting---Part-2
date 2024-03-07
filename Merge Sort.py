def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        # Sort the two halves
        mergeSort(left)
        mergeSort(right)

        # Initial values for pointers that we use to keep track of where we are in each array
        i = 0
        j = 0
        
        # Initial value for the main list
        temp = 0

        # Until we reach the end of either start or end, pick larger among elements start and end
        # and place them in the correct position in the sorted array

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              array[temp] = left[i]
              # Move the iterator forward
              i += 1
            else:
                array[temp] = right[j]
                j += 1
            # Move to the next slot
            temp += 1

        # For all the remaining values When all elements are traversed in either left or right,
        # pick up the remaining elements and put in sorted array.
        while i < len(left):
            array[temp] = left[i]
            i += 1
            temp += 1

        while j < len(right):
            array[temp]=right[j]
            j += 1
            temp += 1

array = [54,26,93,17,77,31,44,55,20]
mergeSort(array)
print(array)
