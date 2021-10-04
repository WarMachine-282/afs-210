def mergeSort(num_list):
    print("Splitting ",num_list) 
    # checks if list if longer than value of 1 then searches for middle point of list
    if len(num_list)>1:
        mid_of_list = len(num_list)//2
        lefthalf = num_list[:mid_of_list]
        righthalf = num_list[mid_of_list:]

        mergeSort(lefthalf) # Merge sorts left half of list
        mergeSort(righthalf) # Merge sorts right half of list
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                num_list[k]=lefthalf[i]
                i=i+1
            else:
                num_list[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            num_list[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            num_list[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",num_list)

num_list = [14,46,43,27,57,41,45,21,70]
mergeSort(num_list)
print(num_list) # prints ordered list

# src https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-8.php