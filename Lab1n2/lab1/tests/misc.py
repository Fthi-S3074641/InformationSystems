import matplotlib.pyplot as plt


def save_timeseries_plot(ts):
    plt.plot(ts)
    plt.ylabel("Time since Start in Seconds")
    plt.xlabel("Number of Images created")
    plt.grid(True, which='both')
    plt.savefig('figure.png')
