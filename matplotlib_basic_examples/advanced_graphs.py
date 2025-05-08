import matplotlib.pyplot as plt
import numpy as np

def plot_3d():
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))
    ax.plot_surface(X, Y, Z, cmap='viridis')
    plt.title("Advanced: 3D Surface Plot")
    plt.show()

def animated_plot():
    import matplotlib.animation as animation
    fig, ax = plt.subplots()
    x = np.linspace(0, 2*np.pi, 100)
    line, = ax.plot(x, np.sin(x))

    def update(frame):
        line.set_ydata(np.sin(x + frame / 10.0))
        return line,

    ani = animation.FuncAnimation(fig, update, frames=100, blit=True)
    plt.title("Advanced: Animated Sine Wave")
    plt.show()

def interactive_plot():
    from matplotlib.widgets import Slider
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    fig, ax = plt.subplots()
    l, = ax.plot(x, y)
    ax_slider = plt.axes([0.2, 0.01, 0.65, 0.03])
    slider = Slider(ax_slider, 'Freq', 0.1, 2.0, valinit=1.0)

    def update(val):
        l.set_ydata(np.sin(slider.val * x))
        fig.canvas.draw_idle()
    slider.on_changed(update)
    plt.title("Advanced: Interactive Plot with Slider")
    plt.show()

def polar_plot():
    theta = np.linspace(0, 2 * np.pi, 100)
    r = np.abs(np.sin(5 * theta))
    plt.figure()
    ax = plt.subplot(111, polar=True)
    ax.plot(theta, r)
    plt.title("Advanced: Polar Plot")
    plt.show()

def contour_plot():
    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.exp(-X**2 - Y**2)
    plt.figure()
    plt.contour(X, Y, Z)
    plt.title("Advanced: Contour Plot")
    plt.show()

def main():
    plot_3d()
    animated_plot()
    interactive_plot()
    polar_plot()
    contour_plot()

if __name__ == "__main__":
    main() 