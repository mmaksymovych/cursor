import matplotlib.pyplot as plt
import numpy as np

# Set style for better looking plots
plt.style.use("ggplot")

# Create sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

# Create a figure with subplots
fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2, figsize=(15, 15))
fig.suptitle("Simple Plots Examples", fontsize=16)

# 1. Basic Line Plot
ax1.plot(x, y1, label="sin(x)", color="blue", linewidth=2)
ax1.set_title("Basic Line Plot")
ax1.set_xlabel("X axis")
ax1.set_ylabel("Y axis")
ax1.grid(True)
ax1.legend()

# 2. Multiple Lines Plot
ax2.plot(x, y1, label="sin(x)", color="blue", linewidth=2)
ax2.plot(x, y2, label="cos(x)", color="red", linewidth=2)
ax2.set_title("Multiple Lines Plot")
ax2.set_xlabel("X axis")
ax2.set_ylabel("Y axis")
ax2.grid(True)
ax2.legend()

# 3. Bar Chart
categories = ["A", "B", "C", "D", "E"]
values = [23, 45, 56, 78, 32]
ax3.bar(categories, values, color="skyblue")
ax3.set_title("Simple Bar Chart")
ax3.set_xlabel("Categories")
ax3.set_ylabel("Values")
ax3.grid(True, axis="y")

# 4. Scatter Plot
x_scatter = np.random.normal(0, 1, 100)
y_scatter = np.random.normal(0, 1, 100)
ax4.scatter(x_scatter, y_scatter, alpha=0.6, c="green")
ax4.set_title("Scatter Plot")
ax4.set_xlabel("X axis")
ax4.set_ylabel("Y axis")
ax4.grid(True)

# 5. Pie Chart
sizes = [30, 20, 25, 15, 10]
labels = ["A", "B", "C", "D", "E"]
ax5.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
ax5.set_title("Pie Chart")
ax5.axis("equal")

# 6. Area Plot
ax6.fill_between(x, y1, y2, alpha=0.3, color="purple")
ax6.plot(x, y1, color="blue", label="sin(x)")
ax6.plot(x, y2, color="red", label="cos(x)")
ax6.set_title("Area Plot")
ax6.set_xlabel("X axis")
ax6.set_ylabel("Y axis")
ax6.grid(True)
ax6.legend()

# Adjust layout and display
plt.tight_layout()
plt.show()
