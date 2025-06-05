import math
from functools import lru_cache


def N_sep(x, x_arr, y_arr):
	sm = y_arr[0]
	for k in range(1, len(x_arr)):
		mul = f(x_arr[:k + 1], y_arr[:k + 1])
		for j in range(k):
			mul *= x - x_arr[j]
		sm += mul
	return sm


def N_non_sep(x, x_arr, y_arr):
	sm = 0
	if x < x_arr[len(x_arr) // 2 - 1]:
		t = (x - x_arr[0]) / (x_arr[1] - x_arr[0])
		sm += y_arr[0]
		for k in range(1, len(x_arr)):
			mul = count_delta(y_arr, k, 0)
			for j in range(k):
				mul *= (t - j)
			sm += mul / math.factorial(k)
	else:
		t = (x - x_arr[-1]) / (x_arr[1] - x_arr[0])
		sm += y_arr[-1]
		for k in range(1, len(x_arr)):
			mul = count_delta(y_arr, k, len(x_arr) - k - 1)
			for j in range(k):
				mul *= (t + j)
			sm += mul / math.factorial(k)
	return sm


def count_delta(y_arr, k, i):
	if k == 1:
		return y_arr[i + 1] - y_arr[i]
	else:
		return count_delta(y_arr, k - 1, i + 1) - count_delta(y_arr, k - 1, i)


def f(x_arr, y_arr):
	if len(x_arr) == 1:
		return y_arr[0]
	else:
		return (f(x_arr[1:], y_arr[1:]) - f(x_arr[:-1], y_arr[:-1])) / (x_arr[-1] - x_arr[0])
