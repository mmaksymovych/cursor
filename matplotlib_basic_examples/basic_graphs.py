import matplotlib.pyplot as plt
import numpy as np

def line_plot():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.figure()
    plt.plot(x, y, label="sin(x)")
    plt.title("Line Plot Example")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

def scatter_plot():
    x = np.random.rand(100)
    y = np.random.rand(100)
    plt.figure()
    plt.scatter(x, y, color='red', alpha=0.5)
    plt.title("Scatter Plot Example")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

def bar_plot():
    categories = ['A', 'B', 'C', 'D']
    values = [10, 24, 36, 18]
    plt.figure()
    plt.bar(categories, values, color='green')
    plt.title("Bar Plot Example")
    plt.xlabel("Category")
    plt.ylabel("Value")
    plt.show()

def main():
    print("Running all basic matplotlib graph examples...")
    line_plot()
    scatter_plot()
    bar_plot()

if __name__ == "__main__":
    main() 