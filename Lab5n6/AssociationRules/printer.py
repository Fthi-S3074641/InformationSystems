import matplotlib.pyplot as plt
import numpy as np


class Printer:
    @classmethod
    def print_histogram(cls, data):
        counts = [np.count_nonzero(col) for col in data]
        counts.sort(reverse=True)
        bins = np.arange(0, data.shape[0], 1)

        plt.bar(bins, counts, 1)
        plt.xlim(0, data.shape[0])
        plt.xlabel('No. of Transaction')
        plt.ylabel('Count of Items in Transaction')
        plt.show()