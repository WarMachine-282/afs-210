def counting_sort(list, max_val):
    m = max_val + 1
    count = [0] * m                
    
    for n in list:
    # count occurences
        count[n] += 1             
    i = 0
    for n in range(m):            
        for c in range(count[n]):  
            list[i] = n
            i += 1
    return list # returns sorted list

print(counting_sort( [1, 2, 7, 3, 2, 1, 4, 2, 3, 2, 1], 7 ))

# src https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-10.php