def L(x: float, x_arr, y_arr):
	sm = 0
	for i in range(len(x_arr)):
		mul = y_arr[i]
		for j in range(len(x_arr)):
			if i == j: continue
			mul *= (x - x_arr[j]) / (x_arr[i] - x_arr[j])
		sm += mul
	return sm
