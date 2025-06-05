import math
import sys

import graph
import lagrange
import newton

n = int(input("Я хочу вот такое количество точек (5-10): "))
if n < 5 or n > 10:
	print("Значение вне диапазона")
	sys.exit(-1)
arr_type = int(input("1 - по произвольным точкам, 2 - с фиксированным шагом, 3 - используя готовую функцию: "))
x_arr = []
y_arr = []
if arr_type == 1:
	print("Начинаем вводить точки:")
	for i in range(n):
		x_i, y_i = map(float, input().split())
		x_arr.append(x_i)
		y_arr.append(y_i)
elif arr_type == 2:
	x0 = float(input("Введите начальный икс: "))
	h = float(input("И шаг: "))
	print("Начинайте вводить игреки:")
	for i in range(n):
		x_arr.append(x0 + h * i)
		y_arr.append(float(input()))
else:
	fn = int(input("Выберите функцию (1 - sinx, 2 - x^2): "))
	if fn == 1:
		fn = lambda x: math.sin(x)
	elif fn == 2:
		fn = lambda x: x ** 2
	else:
		print("Вне диапазона!")
		sys.exit(-1)
	h = float(input("Введите шаг: "))
	x0 = float(input("Введите начальный икс: "))
	for i in range(n):
		x_arr.append(x0 + h * i)
		y_arr.append(fn(x0 + h * i))
x = float(input("Я хочу чтобы мне посчитали значение в точке: "))
if x > x_arr[-1] or x < x_arr[0]:
	print("Внимание! икс лежит вне заданного диапазона")
graph.create_plot()
graph.add_points(x_arr, y_arr, color='black')
fixed_h = True
h = x_arr[1] - x_arr[0]
for i in range(n - 1):
	if x_arr[i + 1] - x_arr[i] != h:
		fixed_h = False
		break
interval = [x_arr[0] - 1, x_arr[-1] + 1]
if fixed_h:
	print("Отлично! У нас фиксированный шаг, можем использовать неразделенные разности!!!")
	graph.add_function(lambda x: newton.N_non_sep(x, x_arr, y_arr), interval, label="Неразделенные разности")
	dot = newton.N_non_sep(x, x_arr, y_arr)
	print(f"Значение рассчитанное по неразделенным: {dot}")
	graph.add_points([x], [dot], label="Неразделенные", color="green")

graph.add_function(lambda x: newton.N_sep(x, x_arr, y_arr), interval, label="Разделенные разности")
dot = newton.N_sep(x, x_arr, y_arr)
print(f"Значение рассчитанное по Ньютону: {dot}")
graph.add_points([x], [dot], label="Разделенные", color="blue")

graph.add_function(lambda x: lagrange.L(x, x_arr, y_arr), interval, label="Лагранж")
dot = lagrange.L(x, x_arr, y_arr)
print(f"Значение рассчитанное по Лагранжу: {dot}")
graph.add_points([x], [dot], label="Лагранж", color="yellow")

graph.show()
