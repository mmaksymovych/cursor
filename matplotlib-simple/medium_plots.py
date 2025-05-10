import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Rectangle, Arrow
from matplotlib.colors import LinearSegmentedColormap

# Set style for better looking plots
plt.style.use("ggplot")

# 1. Multiple Y-axes Plot
fig1 = plt.figure(figsize=(10, 6))
ax1 = fig1.add_subplot(111)
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x) * 100  # Different scale

ax1.plot(x, y1, 'b-', label='sin(x)')
ax1.set_xlabel('X axis')
ax1.set_ylabel('sin(x)', color='b')
ax1.tick_params(axis='y', labelcolor='b')

ax2 = ax1.twinx()
ax2.plot(x, y2, 'r-', label='100*cos(x)')
ax2.set_ylabel('100*cos(x)', color='r')
ax2.tick_params(axis='y', labelcolor='r')

ax1.set_title('Multiple Y-axes')
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right')
plt.tight_layout()

# 2. Custom Styled Scatter Plot
fig2 = plt.figure(figsize=(10, 6))
ax3 = fig2.add_subplot(111)
np.random.seed(42)
x = np.random.normal(0, 1, 50)
y = np.random.normal(0, 1, 50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

scatter = ax3.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')
ax3.set_title('Custom Scatter Plot')
ax3.set_xlabel('X axis')
ax3.set_ylabel('Y axis')
ax3.grid(True, linestyle='--', alpha=0.7)

# Add annotations for some points
for i in range(0, 50, 10):
    ax3.annotate(f'Point {i}', (x[i], y[i]), 
                xytext=(10, 10), textcoords='offset points',
                bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
plt.tight_layout()

# 3. Bar Plot with Error Bars
fig3 = plt.figure(figsize=(10, 6))
ax4 = fig3.add_subplot(111)
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]
errors = [5, 3, 7, 4, 6]

bars = ax4.bar(categories, values, yerr=errors, capsize=10,
               color=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF99CC'])
ax4.set_title('Bar Plot with Error Bars')
ax4.set_xlabel('Categories')
ax4.set_ylabel('Values')

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}',
             ha='center', va='bottom')
plt.tight_layout()

# 4. Line Plot with Fill
fig4 = plt.figure(figsize=(10, 6))
ax5 = fig4.add_subplot(111)
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

ax5.plot(x, y1, 'b-', label='sin(x)', linewidth=2)
ax5.plot(x, y2, 'r--', label='cos(x)', linewidth=2)
ax5.fill_between(x, y1, y2, where=(y1 > y2), color='green', alpha=0.3)
ax5.fill_between(x, y1, y2, where=(y1 <= y2), color='red', alpha=0.3)

ax5.set_title('Line Plot with Fill')
ax5.set_xlabel('X axis')
ax5.set_ylabel('Y axis')
ax5.grid(True, linestyle='--', alpha=0.7)
ax5.legend()

# Add annotations for key points
max_sin = np.argmax(y1)
min_sin = np.argmin(y1)
ax5.annotate('Max', xy=(x[max_sin], y1[max_sin]),
            xytext=(x[max_sin]+1, y1[max_sin]+0.5),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax5.annotate('Min', xy=(x[min_sin], y1[min_sin]),
            xytext=(x[min_sin]+1, y1[min_sin]-0.5),
            arrowprops=dict(facecolor='black', shrink=0.05))
plt.tight_layout()

# Show all plots
plt.show() 