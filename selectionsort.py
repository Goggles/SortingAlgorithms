my_list = [8, 5, 22, 69, 4]

def selection_sort(list):
    sorted = []
    while len(list):
	lowest = list[0]
	for x in list:
	    if x < lowest:
		lowest = x
	sorted.append(lowest)
	list.remove(lowest)
    return sorted

print selection_sort(my_list)