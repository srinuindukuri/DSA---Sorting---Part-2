# function to perform quick sort
def quickSort(arr,low,high):
   if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right

      p = partition(arr,low,high)
      
       # recursive call on the left of pivot
      quickSort(arr, low, p-1)

       # recursive call on the right of pivot
      quickSort(arr, p+1, high)

# function to find partition position
def partition(arr,low,high):
   pivot = arr[high]         # pivot element
   i = ( low-1 )             # pointer for greater element

   # traverse through all elements compare each element with pivot
   for j in range(low , high):

      # if element smaller than pivot is found
      if arr[j] <= pivot:

        # swap it with the greater element pointed by i
         i = i+1 

         # swapping element at i with element at j
         arr[i],arr[j] = arr[j],arr[i] 
    
    # swap the pivot element with the greater element specified by i
   arr[i+1],arr[high] = arr[high],arr[i+1]

   # function to perform quicksort
   return ( i+1 )

# main
arr = [2, 5, 3, 8, 6, 5, 4, 7]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
print(arr)