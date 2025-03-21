def merge_sorted_arrays(arr1, arr2):
    m, n = len(arr1), len(arr2)
    merged_array = []
    i, j = 0, 0

    
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    
    while i < m:
        merged_array.append(arr1[i])
        i += 1

    while j < n:
        merged_array.append(arr2[j])
        j += 1

    return merged_array


arr1 = list(map(int, input("Enter sorted elements of arr1 : ").split()))
arr2 = list(map(int, input("Enter sorted elements of arr2 : ").split()))


result = merge_sorted_arrays(arr1, arr2)
print("Merged Sorted Array:", result)
 
