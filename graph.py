import numpy as np
import matplotlib.pyplot as plt

best_approx = None

def create_plot(figsize=(10, 6)):
	plt.figure(figsize=figsize)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.grid(True, alpha=0.3)


def add_function(func, interval, label=None, color=None, is_best=False):
	if func is None:
		return
	linestyle = '-' if is_best else '--'
	if is_best:
		global best_approx
		best_approx = label
	a, b = interval
	x = np.linspace(a, b, 500)
	y = np.vectorize(func)(x)

	plt.plot(x, y,
			 label=label,
			 color=color,
			 linestyle=linestyle,
			 zorder=1)


def add_points(x_arr, y_arr, label=None, color='red', marker_size=100):
	x_points = np.array(x_arr)
	y_points = np.array(y_arr)

	plt.scatter(x_points, y_points,
				color=color,
				s=marker_size,
				zorder=2,
				label=label,
				edgecolors='black')


def show():
	plt.title('Графики приближений')
	plt.legend()
	plt.show()