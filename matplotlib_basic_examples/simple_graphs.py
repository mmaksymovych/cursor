import matplotlib.pyplot as plt
import numpy as np

def line_plot():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.figure()
    plt.plot(x, y)
    plt.title("Simple: Line Plot")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.show()

def scatter_plot():
    x = np.random.rand(100)
    y = np.random.rand(100)
    plt.figure()
    plt.scatter(x, y)
    plt.title("Simple: Scatter Plot")
    plt.show()

def bar_plot():
    categories = ['A', 'B', 'C', 'D']
    values = [10, 24, 36, 18]
    plt.figure()
    plt.bar(categories, values)
    plt.title("Simple: Bar Plot")
    plt.show()

def histogram():
    data = np.random.randn(1000)
    plt.figure()
    plt.hist(data, bins=30)
    plt.title("Simple: Histogram")
    plt.show()

def pie_chart():
    sizes = [15, 30, 45, 10]
    labels = ['A', 'B', 'C', 'D']
    plt.figure()
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("Simple: Pie Chart")
    plt.show()

def main():
    line_plot()
    scatter_plot()
    bar_plot()
    histogram()
    pie_chart()

if __name__ == "__main__":
    main() 