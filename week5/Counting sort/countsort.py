def counting_sort(array, max_val):
    m = max_val + 1
    count = [0] * m                
    
    for a in array:
    # count occurences
        count[a] += 1             
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            array[i] = a
            i += 1
    return array # returns sorted array

print(counting_sort( [1, 2, 7, 3, 2, 1, 4, 2, 3, 2, 1], 7 ))

# src https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-10.php