import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LinearSegmentedColormap

# Set style for better looking plots
plt.style.use("ggplot")

# 1. 3D Surface Plot
fig1 = plt.figure(figsize=(10, 8))
ax1 = fig1.add_subplot(111, projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

surf = ax1.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True)
ax1.set_title('3D Surface Plot')
ax1.set_xlabel('X axis')
ax1.set_ylabel('Y axis')
ax1.set_zlabel('Z axis')
fig1.colorbar(surf, ax=ax1, shrink=0.5, aspect=5)
plt.tight_layout()

# 2. 3D Scatter Plot with Color Gradient
fig2 = plt.figure(figsize=(10, 8))
ax2 = fig2.add_subplot(111, projection='3d')
n = 100
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
z = np.random.normal(0, 1, n)
colors = np.random.rand(n)

scatter = ax2.scatter(x, y, z, c=colors, cmap='viridis', s=100)
ax2.set_title('3D Scatter Plot')
ax2.set_xlabel('X axis')
ax2.set_ylabel('Y axis')
ax2.set_zlabel('Z axis')
fig2.colorbar(scatter, ax=ax2)
plt.tight_layout()

# 3. Polar Plot with Custom Styling
fig3 = plt.figure(figsize=(10, 8))
ax3 = fig3.add_subplot(111, projection='polar')
theta = np.linspace(0, 2*np.pi, 100)
r = 2 + np.sin(3*theta)

ax3.plot(theta, r, 'b-', linewidth=2)
ax3.fill(theta, r, alpha=0.3)
ax3.set_title('Polar Plot')
ax3.grid(True, linestyle='--', alpha=0.7)

# Add annotations for key points
max_r = np.argmax(r)
min_r = np.argmin(r)
ax3.annotate('Max', xy=(theta[max_r], r[max_r]),
            xytext=(theta[max_r]+0.5, r[max_r]+0.5),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax3.annotate('Min', xy=(theta[min_r], r[min_r]),
            xytext=(theta[min_r]+0.5, r[min_r]-0.5),
            arrowprops=dict(facecolor='black', shrink=0.05))
plt.tight_layout()

# 4. Complex Line Plot with Multiple Features
fig4 = plt.figure(figsize=(10, 8))
ax4 = fig4.add_subplot(111)
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

# Create custom colormap
colors = [(0, 'red'), (0.5, 'green'), (1, 'blue')]
cmap = LinearSegmentedColormap.from_list('custom_cmap', colors)

# Plot with gradient color
for i in range(len(x)-1):
    ax4.plot(x[i:i+2], y1[i:i+2], color=cmap(i/len(x)), linewidth=2)

# Add second line with different style
ax4.plot(x, y2, 'r--', linewidth=2, label='cos(x)')

# Add third line with fill
ax4.plot(x, y3, 'g-', linewidth=2, label='sin(x)*cos(x)')
ax4.fill_between(x, y3, alpha=0.3, color='green')

# Customize the plot
ax4.set_title('Complex Line Plot')
ax4.set_xlabel('X axis')
ax4.set_ylabel('Y axis')
ax4.grid(True, linestyle='--', alpha=0.7)
ax4.legend()

# Add annotations for key points
max_y1 = np.argmax(y1)
min_y1 = np.argmin(y1)
ax4.annotate('Max', xy=(x[max_y1], y1[max_y1]),
            xytext=(x[max_y1]+0.5, y1[max_y1]+0.5),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax4.annotate('Min', xy=(x[min_y1], y1[min_y1]),
            xytext=(x[min_y1]+0.5, y1[min_y1]-0.5),
            arrowprops=dict(facecolor='black', shrink=0.05))
plt.tight_layout()

# Show all static plots
plt.show()

# Create an animation in a separate window
fig_anim = plt.figure(figsize=(10, 6))
ax_anim = fig_anim.add_subplot(111)
x = np.linspace(0, 2*np.pi, 100)
line, = ax_anim.plot(x, np.sin(x))
ax_anim.set_title('Animated Sine Wave')
ax_anim.set_xlabel('X axis')
ax_anim.set_ylabel('Y axis')
ax_anim.grid(True)

def animate(frame):
    line.set_ydata(np.sin(x + frame/10))
    return line,

anim = FuncAnimation(fig_anim, animate, frames=100, interval=50, blit=True)
plt.show() 