def binary_search(mylist, target):
	low = 0
	high = len(mylist)-1
	while low <= high:
		mid = (low+high)//2
		if mylist[mid] == target:
			return mid+1
		elif mylist[mid] < target:
			low = mid + 1
		else:
			high = mid - 1
	return -1