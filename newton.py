def N_sep(x, x_arr, y_arr):
	sm = y_arr[0]
	for k in range(1, len(x_arr)):
		mul = f(x_arr[:k+1], y_arr[:k+1])
		for j in range(k):
			mul *= x - x_arr[j]
		sm += mul
	return sm


def f(x_arr, y_arr):
	if len(x_arr) == 1:
		return y_arr[0]
	else:
		return (f(x_arr[1:], y_arr[1:]) - f(x_arr[:-1], y_arr[:-1])) / (x_arr[-1] - x_arr[0])
