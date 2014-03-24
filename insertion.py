#insertion sort algorithm. without loops.

def insertion(arr, pos=0):

	if pos == len(arr):
		return

	if pos == 0:
		insertion(arr, 1)
		return arr

	current = arr[pos]
	previous = arr[pos-1]

	if current < previous:
		arr[pos] = previous
		arr[pos - 1] = current
		insertion(arr, pos - 1)
	else:
		insertion(arr, pos + 1)


if __name__ == "__main__":
	print insertion([1,2,4,54,132,52,3,5,456,23,656546,12])