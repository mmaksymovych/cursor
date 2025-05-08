import matplotlib.pyplot as plt
import numpy as np

def stacked_bar_plot():
    categories = ['A', 'B', 'C', 'D']
    values1 = [10, 20, 30, 40]
    values2 = [5, 15, 25, 35]
    plt.figure()
    plt.bar(categories, values1, label='Set 1')
    plt.bar(categories, values2, bottom=values1, label='Set 2')
    plt.title("Medium: Stacked Bar Plot")
    plt.legend()
    plt.show()

def box_plot():
    data = [np.random.normal(0, std, 100) for std in range(1, 4)]
    plt.figure()
    plt.boxplot(data)
    plt.title("Medium: Box Plot")
    plt.show()

def violin_plot():
    data = [np.random.normal(0, std, 100) for std in range(1, 4)]
    plt.figure()
    plt.violinplot(data)
    plt.title("Medium: Violin Plot")
    plt.show()

def multiple_lines():
    x = np.linspace(0, 10, 100)
    plt.figure()
    plt.plot(x, np.sin(x), label='sin(x)')
    plt.plot(x, np.cos(x), label='cos(x)')
    plt.title("Medium: Multiple Line Plots")
    plt.legend()
    plt.show()

def subplots():
    x = np.linspace(0, 10, 100)
    fig, axs = plt.subplots(2)
    axs[0].plot(x, np.sin(x))
    axs[0].set_title('sin(x)')
    axs[1].plot(x, np.cos(x), 'r')
    axs[1].set_title('cos(x)')
    plt.tight_layout()
    plt.show()

def error_bar():
    x = np.arange(0, 10, 1)
    y = np.exp(-x/3.0)
    error = 0.1 + 0.2 * x
    plt.figure()
    plt.errorbar(x, y, yerr=error, fmt='-o')
    plt.title("Medium: Error Bar Plot")
    plt.show()

def heatmap():
    data = np.random.rand(10, 10)
    plt.figure()
    plt.imshow(data, cmap='hot', interpolation='nearest')
    plt.title("Medium: Heatmap")
    plt.colorbar()
    plt.show()

def main():
    stacked_bar_plot()
    box_plot()
    violin_plot()
    multiple_lines()
    subplots()
    error_bar()
    heatmap()

if __name__ == "__main__":
    main() 