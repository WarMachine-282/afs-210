import heapq as hq
# original list 
list = [25, 35, 22, 85, 14, 65, 75, 22, 58]
print("Original List:", list)
# three largest numbers 
largest_numbers = hq.nlargest(3, list)
print("Three largest numbers are:", largest_numbers)