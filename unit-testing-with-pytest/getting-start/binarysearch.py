def binary_search(mylist, target):
	low = 0
	high = len(mylist)-1
	while low <= high:
		mid = (low+high)//2
		if mylist[mid] == target:
			return mid
		elif mylist[mid] < target:
			low = mid + 1
		else:
			high = mid - 1
	print("can't find")
	return -1