my_list = [12, 10, 5, 18, 44, 1]

def bubble_sort(list):
    i = 0
    is_sorted = False
    length = len(list) - 1
    while not is_sorted:
	is_sorted = True
	for i in xrange(length):
	    if list[i] > list[i + 1]: #check the list item is greater than the next one
		#the list isn't sorted
		is_sorted = False
		#re-arrange list elements accordingly
		hold = list[i + 1] 
		list[i + 1] = list[i]
		list[i] = hold

bubble_sort(my_list)
print my_list