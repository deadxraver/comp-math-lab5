import math

DELTA_CACHE = []
cached = False

def N_sep(x, x_arr, y_arr):
	sm = y_arr[0]
	for k in range(1, len(x_arr)):
		mul = f(x_arr[:k + 1], y_arr[:k + 1])
		for j in range(k):
			mul *= x - x_arr[j]
		sm += mul
	return sm


def N_non_sep(x, x_arr, y_arr, print_deltas=False):
	global cached
	global DELTA_CACHE
	if not cached:
		DELTA_CACHE = [[None] * (len(x_arr) - i) for i in range(len(x_arr))]
		for i in range(len(DELTA_CACHE)):
			DELTA_CACHE[i][0] = y_arr[i]
			for k in range(1, len(x_arr) - i):
				DELTA_CACHE[i][k] = (count_delta(y_arr, k, i))
		cached = True
	if print_deltas:
		print('Таблица конечных разностей')
		for i in range(len(DELTA_CACHE)):
			print(DELTA_CACHE[i])
	sm = 0
	if x < x_arr[len(x_arr) // 2 - 1]:
		t = (x - x_arr[0]) / (x_arr[1] - x_arr[0])
		sm += y_arr[0]
		for k in range(1, len(x_arr)):
			mul = DELTA_CACHE[0][k]
			for j in range(k):
				mul *= (t - j)
			sm += mul / math.factorial(k)
	else:
		t = (x - x_arr[-1]) / (x_arr[1] - x_arr[0])
		sm += y_arr[-1]
		for k in range(1, len(x_arr)):
			mul = DELTA_CACHE[len(x_arr) - k - 1][k]
			for j in range(k):
				mul *= (t + j)
			sm += mul / math.factorial(k)
	return sm


def count_delta(y_arr, k, i):
	if DELTA_CACHE[i][k] is None:
		if k == 0:
			DELTA_CACHE[i][k] = y_arr[i]
			return DELTA_CACHE[i][k]
		if k == 1:
			DELTA_CACHE[i][k] = y_arr[i + 1] - y_arr[i]
		else:
			DELTA_CACHE[i][k] = count_delta(y_arr, k - 1, i + 1) - count_delta(y_arr, k - 1, i)
	return DELTA_CACHE[i][k]


def f(x_arr, y_arr):
	if len(x_arr) == 1:
		return y_arr[0]
	else:
		return (f(x_arr[1:], y_arr[1:]) - f(x_arr[:-1], y_arr[:-1])) / (x_arr[-1] - x_arr[0])
