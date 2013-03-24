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

my_list = []

while True:
	input = raw_input("Enter a number to be added to the list (enter sort to end adding and sort the list): ")
	if input == 'sort':
		break
	elif input.isdigit():
		my_list.append(input)
	else:
		print "Please enter a number, or sort."

bubble_sort(my_list)
print my_list
