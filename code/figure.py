import matplotlib.pyplot as plt

def plot(x, y):
    plt.plot(x,y)
    plt.savefig('./src/figures/figure.png')

plot([1, 2, 3], [1, 4, 9])