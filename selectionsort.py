my_list = [8, 5, 22, 69, 4]

def selection_sort(list):
    sorted_list = []
    while len(list):
	lowest = list[0]
	for x in list:
	    if x < lowest:
		lowest = x
	sorted_list.append(lowest)
	list.remove(lowest)
    return sorted_list

print selection_sort(my_list)