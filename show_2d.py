import numpy as np 
import matplotlib.pyplot as plt

'''
#H = np.array([[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]])
'''


def show_2d_plot(two_d_array, name='plot'):
    H = np.array(two_d_array)
    plt.imshow(H, interpolation='none')
    plt.title(name)
    plt.show()
