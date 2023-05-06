def binary_search(arr, target):
	# find the index of the given target. If target is not in arr, return the index where it should be
	# inserted
	left, right = 0, len(arr) - 1
	while left <= right:
		mid = (left + right) // 2
		if arr[mid] == target:
			return mid
		elif arr[mid] > target:
			right = mid - 1
		else:
			left = mid + 1

	# the new index where target should be inserted but still maintains the order of sorted arr
	return left


if __name__ == '__main__':
	assert binary_search([1, 2, 3, 4], 1) == 0
	assert binary_search([1, 10, 20, 30, 35], 12) == 2
	assert binary_search([100], 100) == 0
	assert binary_search([12, 23], 25) == 2
